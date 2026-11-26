# ros2_control Hardware Interface

`rby1_hardware/RBY1SystemHardware` is a `ros2_control` `SystemInterface` plugin.
A controller manager (`ros2_control_node`) loads it from the `<ros2_control>` block of the robot's URDF and runs the standard controllers on it: a `joint_trajectory_controller` per part and a `joint_state_broadcaster`.
MoveIt uses it through `demo.launch.py` of the `rby1_moveit_*` packages ([MoveIt 2](rby1_moveit2.md)). It also works without MoveIt, as described below.

## How it works

- **Two connections.** The plugin opens its own gRPC connection to the robot for the command streams, and talks to the running **driver** for the rest.
  On activation it calls `/rby1/robot_power` and `/rby1/robot_servo` (default `all`) and claims the **control right** with `/rby1/hardware_control` (`state: true`).
- **Control right.** While the plugin holds the right, the driver refuses its own command sources (actions, streams, the examples) and keeps publishing the state.
  On deactivation the plugin cancels its control, closes its streams, disables the Control Manager and releases the right.
- **Streams.** One SDK command stream for the upper body (torso, arms, head) and one for the mobile base. The plugin sends the latest commanded position of every joint at the controller manager's rate (100 Hz in the shipped `ros2_controllers.yaml`).
- **Joints.** Each URDF joint is mapped to an SDK joint by name. One position command interface, and position and velocity state interfaces, per joint.
  A joint the SDK does not have (the finger joints of an M v1.3 model) is not sent to the robot.

::: danger Match the package to the robot
A `rby1_moveit_*` package of another model or version than the robot gives `ros2_control` and the robot different kinematics,
which can send unexpected commands to the robot. Match the package to the robot's model and version before you run on real hardware.
On activation the plugin compares the model and version of its URDF with what the robot reports and refuses to activate on a mismatch
(`[MODEL/VERSION MISMATCH]`). The model comparison is a loose text match, so do not rely on this check alone.
:::

## Using it without MoveIt

`rby1_hardware.launch.py` starts the controller manager with the robot's URDF, `robot_state_publisher`, the `joint_state_broadcaster` and the trajectory controllers. Nothing of MoveIt runs.
The driver must be running first.

::: warning
Trajectories sent to the controllers move the robot. Try them with `use_fake_hardware:=true` or in the simulator first, and keep the E-Stop within reach.
:::

```bash
# terminal 1: the driver
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=192.168.30.1:50051 model:=m

# terminal 2
ros2 launch rby1_hardware rby1_hardware.launch.py model:=m version:=1.2 robot_ip:=192.168.30.1:50051
ros2 launch rby1_hardware rby1_hardware.launch.py model:=m version:=1.2                            # simulator on this PC
ros2 launch rby1_hardware rby1_hardware.launch.py model:=m version:=1.2 use_fake_hardware:=true    # no robot, no driver
```

| Argument | Default | Description |
|---|---|---|
| `model`, `version` | required | Robot model (`a`, `m`) and version (the robot's: `1.0` to `1.2` for `a`, `1.0` to `1.3` for `m`). They pick `rby1_moveit_<model>_<version>`, whose URDF and `config/ros2_controllers.yaml` are used |
| `robot_ip` | `127.0.0.1:50051` | Robot address and gRPC port, the same as the driver's |
| `driver_namespace` | `rby1` | Namespace of the running driver |
| `use_fake_hardware` | `false` | `true`: `mock_components/GenericSystem` instead of the robot |

The controllers started active are set by `CONTROLLERS` at the top of `rby1_hardware/launch/rby1_hardware.launch.py`
(default: `right_arm_controller`, `left_arm_controller`, `torso_controller`, `head_controller`).

From then on it is plain `ros2_control`: joint states on `/joint_states`, trajectories to `/<controller>/follow_joint_trajectory` (`control_msgs/action/FollowJointTrajectory`).

```bash
ros2 control list_controllers
ros2 control switch_controllers --deactivate right_arm_controller --activate both_arms_controller

ros2 action send_goal /right_arm_controller/follow_joint_trajectory control_msgs/action/FollowJointTrajectory \
  "{trajectory: {joint_names: [right_arm_0, right_arm_1, right_arm_2, right_arm_3, right_arm_4, right_arm_5, right_arm_6],
     points: [{positions: [0.0, -0.1, 0.0, -0.3, 0.0, 0.0, 0.0], time_from_start: {sec: 3}}]}}"
```

- Two active controllers cannot share a joint: `both_arms_controller` and `right_arm_controller` do not run together.
- Ctrl+C on the launch deactivates the plugin and returns the control right to the driver.
- Do not run it together with a MoveIt `demo.launch.py`: one controller manager per robot.
- In [Bringup](bringup.md) this is the `ROS2_CONTROL` flag.

## Real-time scheduling

`ros2_control_node` sets `SCHED_FIFO` priority 50 for itself at start when the user is allowed to; otherwise it warns and runs with normal scheduling.
To allow it, give the user real-time rights and log in again:

```bash
echo "$USER - rtprio 99" | sudo tee /etc/security/limits.d/99-realtime.conf
echo "$USER - memlock unlimited" | sudo tee -a /etc/security/limits.d/99-realtime.conf
```

The log then says `Successful set up FIFO RT scheduling policy with priority 50`.

Verified against: rby1-ros2 v1.0.0 `rby1_hardware/src/rby1_system_hardware.cpp`, `rby1_hardware/launch/rby1_hardware.launch.py`, `Doc/manual/05_hardware_interface.md`.
