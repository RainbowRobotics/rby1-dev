# MoveIt 2

## RB-Y1 Hardware and MoveIt

The `rby1_hardware` package provides a `ros2_control` `SystemInterface` plugin (`rby1_hardware/RBY1SystemHardware`) that connects MoveIt 2 to the robot through the standard `ros2_control` pipeline.
Each `rby1_moveit_*` package contains the complete MoveIt 2 configuration (SRDF, kinematics, joint limits, controller configs) for one model and version, with a `demo.launch.py`.

This page covers `demo.launch.py`: MoveIt with `ros2_control`, driven from the RViz MotionPlanning panel.
To send tool pose targets from your own node and run plans through the driver instead, see the [MoveIt Planner](moveit_planner.md).
Only one `move_group` can run per ROS domain, so the two do not run together.

<img :src="$withBase('/images/ros2/moveit_gui.png')" alt="" class="center white-bg" style="width:100%">

## Available MoveIt Packages

| Package | Model | Version |
|---------|-------|---------|
| `rby1_moveit_a_1_0` | RB-Y1 A | 1.0 |
| `rby1_moveit_a_1_1` | RB-Y1 A | 1.1 |
| `rby1_moveit_a_1_2` | RB-Y1 A | 1.2 |
| `rby1_moveit_m_1_0` | RB-Y1 M | 1.0 |
| `rby1_moveit_m_1_1` | RB-Y1 M | 1.1 |
| `rby1_moveit_m_1_2` | RB-Y1 M | 1.2 |
| `rby1_moveit_m_1_3` | RB-Y1 M | 1.3 (the gripper is in its model) |

## Launch MoveIt with Real Hardware

::: info Real hardware needs the driver
**Real hardware mode** requires `rby1_driver` to be running first.
On activation, `RBY1SystemHardware` takes the control right from the driver with the `/rby1/hardware_control` service.
Give `demo.launch.py` the same `robot_ip` as the driver; you do not need to edit any launch file.
:::

::: danger Version mismatch risk
If the `rby1_moveit_*` package does not match the robot's model and version, MoveIt and the robot run with different joint and kinematic configurations, which can send unexpected commands to the robot.
**Always make sure the `rby1_moveit_*` package matches the robot's model and version before you launch with real hardware.**
On activation the `rby1_hardware` plugin compares the model and version of the package's URDF with what the robot reports and refuses to activate on a mismatch (`[MODEL/VERSION MISMATCH]`).
The model comparison is a loose text match, so do not rely on this check alone.
:::

::: warning Check a planned trajectory before it runs
OMPL is a sampling planner: the same goal can give a different path each time, and a path can swing a joint far round, flip the elbow,
or pass close to the body or a table, even when start and goal are near. MoveIt checks the path only against what is in its planning scene.
- Watch the planned path in RViz (MotionPlanning, Planned Path) before you execute it.
- Start with `use_fake_hardware:=true` or in the simulator.
- On the robot, keep velocity and acceleration scaling low (the panel's default here is 0.1) and the E-Stop within reach.
:::

**Step 1**: Start the driver (first terminal), with your robot's address and model:

```bash
source install/setup.bash
ros2 launch rby1_driver rby1_ros2_driver.launch.py robot_ip:=192.168.30.1:50051 model:=m
```

**Step 2**: Launch MoveIt (second terminal), with the package that matches your model and version:

```bash
source install/setup.bash

# Real hardware, same address as the driver
ros2 launch rby1_moveit_m_1_2 demo.launch.py robot_ip:=192.168.30.1:50051

# Simulator on this PC (default robot_ip 127.0.0.1:50051)
ros2 launch rby1_moveit_m_1_2 demo.launch.py

# Fake hardware (no robot, no driver needed)
ros2 launch rby1_moveit_m_1_2 demo.launch.py use_fake_hardware:=true
```

Replace `rby1_moveit_m_1_2` with the package matching your robot.
When the log shows `You can start planning now`, plan and execute from the MotionPlanning panel in RViz.
The launch ends when `ros2_control_node` or `move_group` exits. Ctrl+C returns the control right to the driver.

## Launch Arguments

| Argument | Default | Description |
|----------|---------|-------------|
| `use_fake_hardware` | `false` | `true` = `mock_components/GenericSystem` (no robot needed); `false` = `RBY1SystemHardware` (real robot or simulator) |
| `robot_ip` | `127.0.0.1:50051` | Robot gRPC address and port. Must be the same as the driver's `robot_ip` |
| `model` | the package's model (`a` in `rby1_moveit_a_*`, `m` in `rby1_moveit_m_*`) | Robot model passed to the hardware plugin |
| `driver_namespace` | `rby1` | Namespace of the robot driver node, its topics and services |

## ros2_control Controllers

Each package's `config/ros2_controllers.yaml` defines these controllers (update rate 100 Hz):

| Controller | Type | Controlled Joints | Packages |
|------------|------|-------------------|----------|
| `right_arm_controller` | `JointTrajectoryController` | `right_arm_0` to `right_arm_6` | all |
| `left_arm_controller` | `JointTrajectoryController` | `left_arm_0` to `left_arm_6` | all |
| `torso_controller` | `JointTrajectoryController` | `torso_0` to `torso_5` | all |
| `head_controller` | `JointTrajectoryController` | `head_0`, `head_1` | all |
| `both_arms_controller` | `JointTrajectoryController` | all joints of both arms (14) | all |
| `body_controller` | `JointTrajectoryController` | torso, head and both arms (22) | all |
| `gripper_r_controller` | `GripperActionController` | `gripper_finger_r1_joint` | `rby1_moveit_m_1_3` only |
| `gripper_l_controller` | `GripperActionController` | `gripper_finger_l1_joint` | `rby1_moveit_m_1_3` only |
| `joint_state_broadcaster` | `JointStateBroadcaster` | all | all |

`demo.launch.py` starts the controllers listed in the package's `config/moveit_controllers.yaml`: `right_arm_controller`, `left_arm_controller`, `torso_controller` and `head_controller`
(and the two gripper controllers in `rby1_moveit_m_1_3`), plus `joint_state_broadcaster`.
Two active controllers cannot share a joint, so `both_arms_controller` and `body_controller` are not started with them.
To use `ros2_control` controllers without MoveIt, see [ros2_control Hardware Interface](hardware_interface.md).

On M v1.3 the finger joints need the gripper driver's joint states ([Tools](tools.md#gripper)).

Verified against: rby1-ros2 v1.0.0 `rby1_moveit/rby1_moveit_*/launch/demo.launch.py`, `rby1_moveit/rby1_moveit_*/config/ros2_controllers.yaml`, `rby1_moveit/rby1_moveit_*/config/moveit_controllers.yaml`, `rby1_hardware/src/rby1_system_hardware.cpp`, `Doc/manual/06_moveit.md`, `Doc/manual/05_hardware_interface.md`.
