<a id="troubleshooting"></a>
# Troubleshooting & Known Issues

## Issue: The build stops at `RBY1_SDK_PATH`

* **Symptom**: `colcon build` stops in `rby1_driver` or `rby1_hardware` with a message about `RBY1_SDK_PATH`.

* **Resolution**: The variable is not set, or it does not point at a built C++ SDK. The SDK source tree must have
  `include/rby1-sdk/robot.h` and its build in `build/src`. Set it in `~/.bashrc`, open a new terminal and build again
  ([Install & Build](install_and_build.md#2-build-the-c-sdk)).

  ```bash
  export RBY1_SDK_PATH=$HOME/rby1-sdk    # where you cloned and built the SDK
  ```

## Issue: The driver cannot connect to the robot

* **Symptom**: The driver logs a connection error at start and exits.

* **Resolution**:
  - Check `robot_ip` (address **and** port `50051`) in `driver_parameters.yaml` or on the command line (`robot_ip:=192.168.30.1:50051`).
  - Check that the PC reaches the robot PC (RPC): `ping <robot IP>`.
  - For the simulator, check that its container is running, and use `robot_ip:=localhost:50051`.
  - Check that `model` matches the robot or the simulator image (`a` or `m`).

## Issue: Services time out, topics from another robot appear, or `sequence size exceeds remaining buffer`

* **Cause**: Another ROS 2 machine on the same network uses the same `ROS_DOMAIN_ID` (0 when it is not set), and its nodes and message types mix with yours.

* **Resolution**: Give this PC, and every container and PC that talks to the driver, a domain of its own:

  ```bash
  echo 'export ROS_DOMAIN_ID=77' >> ~/.bashrc
  source ~/.bashrc
  ```

  Or keep discovery on one PC when everything runs on it: `ROS_LOCALHOST_ONLY=1` on Humble, `ROS_AUTOMATIC_DISCOVERY_RANGE=LOCALHOST` on Jazzy (`ROS_LOCALHOST_ONLY` is deprecated there). `ros2 node list` must show `/rby1/rby1_ros2_driver` from every terminal you use.

## Issue: A command toward the robot is refused

* **Resolution**: The answer says why. The common causes:
  - Power or servo is off (`Robot is disabled (power/servo is off)`): switch them on with `robot_power` and `robot_servo`. The driver resets a Control Manager fault and enables the Control Manager by itself.
  - The fault reset or the enable failed (`Control Manager Error`): read the driver log for the reason, and find the cause of the fault before you send another motion command.
  - A stream channel the command needs is closed: open it with `stream_control`, or close every channel ([Command Streams](command_streams.md)).
  - The `ros2_control` hardware plugin holds the control right: stop its controller manager, or call `/rby1/hardware_control` with `state: false`.
  - A trajectory's first point cannot be reached in its time.

## Issue: Commands rejected after a streaming node stopped

* **Symptom**:
  A stream-based control node was killed mid-operation. The channels it opened stay open, and the driver refuses other joint or Cartesian commands.
  The driver closes by itself only a channel that got no command within 60 s of being opened.

* **Resolution**:
  Close the channels with `/rby1/stream_control` and `state: false` in a separate terminal:

  ```bash
  ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: false}"
  ```

## Issue: A freshly started simulator refuses to enable

* **Cause**: It may start in a fault, or with a joint outside its limit.

* **Resolution**: Call `robot_power` and `robot_servo` with `parameters: all`, then `control_manager_command` with `command: 1`.
  A joint over its limit needs `command: 4` (`CMD_UNLIMIT`) once, then a move back inside, for example with `06_zero_pose`.

## Issue: "Collision detected!" Warning

* **Symptom**:
  The driver logs `Collision detected! Distance: ... (Links: ... <-> ...)` once, and `robot_state.collision` is `true`.
  This is common in simulation when the initial joint state puts links close together.

* **What the driver does**:
  The driver only reports the collision. It does **not** stop the robot, cancel the command or shut down.
  A collision is reported when the smallest link distance is below `collision_threshold` (see [Driver Parameters](config_driver_parameters.md)).

* **Resolution**:
  Move the robot to a pose where the links are apart. If your application must stop on a collision,
  watch `robot_state.collision` and stop the motion yourself (example `14_collision_safety_control`).
  Do not set `collision_threshold` to `0.0` to hide the warning: it turns off the report your application relies on.

## Issue: Client-Side Warnings `Ignoring unexpected goal/result response`

* **Symptom**:
  A sequential Python client prints `Ignoring unexpected goal response. There may be more than one action server for the action 'robot_joint'` or `Ignoring unexpected result response`.

* **Cause**:
  `time.sleep()` blocks the client's executor, so DDS answers pile up and are processed out of order at the next spin.
  With a stream channel open, `robot_joint` goals also finish quickly, which makes this more likely.

* **Resolution**:
  Do not use `time.sleep()` in a node that waits between goals. Spin while you wait, as `13_stream_command` does:

  ```python
  import time
  import rclpy

  def spin_sleep(node, duration_s: float) -> None:
      """Wait without blocking the executor, so goal and result answers keep being processed."""
      end = time.monotonic() + duration_s
      while rclpy.ok() and time.monotonic() < end:
          rclpy.spin_once(node, timeout_sec=0.01)
  ```

## Issue: MoveIt Known Issues

### Warning: `Missing gripper_finger_r2_joint` / `gripper_finger_l2_joint`

```
[WARN] The complete state of the robot is not yet known. Missing gripper_finger_r2_joint
```

**Cause**: On a model with the gripper in its URDF (M v1.3), `gripper_finger_r2_joint` and `gripper_finger_l2_joint` are **mimic joints** (linked to `r1`/`l1` with `<mimic>`) and are not registered in `ros2_control`. The `joint_state_broadcaster` does not publish state for them, so MoveIt's planning scene monitor raises this warning.

**Impact**: **None**. Planning and execution for all controlled joints work. This warning can be ignored.

### Hardware Control Handoff

When `demo.launch.py` of a `rby1_moveit_*` package runs with real hardware, the `RBY1SystemHardware` plugin calls `/rby1/hardware_control` with `state: true` to take the control right from the driver.
During this time the driver rejects its own command sources (for example `robot_joint` and the examples). The control right returns to the driver when MoveIt is shut down (Ctrl+C).

### `move_group` dies with a segmentation fault on Ctrl+C

MoveIt 2.5.9 (Humble) unloads its controller plugin before the node that plugin built. The [MoveIt planner](moveit_planner.md) launch preloads the library so `move_group` exits cleanly; the `demo.launch.py` files do not. The crash happens at shutdown only.

Verified against: rby1-ros2 v1.0.0 `Doc/manual/01_overview.md` (Troubleshooting), `Doc/manual/03_examples.md`, `rby1_driver/CMakeLists.txt`, `rby1_examples/rby1_examples/13_stream_command.py`.
