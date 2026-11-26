# Software Architecture

## System Overview

The software architecture ensures stable performance and safety while providing scalability for the robot. It is designed to cover various application needs and enables quick and efficient development of custom solutions through its scalable structure.

<img :src="$withBase('/images/software/architecture/rby-software-stack-white.png')" alt="rby-software-stack-white" class="center white-bg" style="width:600px">

<p style="text-align:center;">
[ Software architecture of RB-Y1 ]
</p>

This architecture is composed as follows:

- **Independent robot internal controllers (robot PC, RPC)**: Ensures stable performance and safety. It operates alongside the application control PC (user PC, UPC) to offer scalability.
  See [Robot Main Program](robot_main_program.md) for the program on the RPC and [User PC (UPC)](upc.md) for the UPC.

- **Non-realtime communication channels**: Designed for high-level commands and robot settings, such as power management. These channels use **Google gRPC** (port 50051), allowing commands to be built using a builder pattern and executed at up to **100Hz**. Two types of communication patterns are available:

    1. **Once**: Suitable for executing a single command at a time, such as setting a target position or velocity. This method is used for one-time commands that do not require continuous updates.

    2. **Stream**: Designed for continuous command exchange, ideal for tasks where frequent updates are necessary. If you need to send and receive commands regularly, Stream mode is recommended for maintaining smooth operations.

    Available controllers include:

    - Joint Position Control
    - Joint Velocity Control
    - Cartesian Control
    - Gravity Compensation Control
    - Optimal Control
    - Impedance Control
    - SE2 Velocity Control

    The full list, and which part of the robot accepts which controller, is in [Command and Control Architecture](../sdk/controllers/generated/command_and_control_architecture.md#controllers).
    The builders are defined in [`robot_command_builder.h`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/include/rby1-sdk/robot_command_builder.h).

- **Realtime command channels**: Focused on low-level, time-sensitive commands with responses at 500Hz (2 ms) using UDP. Users can implement their own position or torque controllers for real-time operations.
  See [`real_time_control.max_timeout_count`](../sdk/controllers/generated/parameter.md#real_time_controlmax_timeout_count) for what happens when packets are late.

- **A robot model library**: Provides access to the robot's kinematic and dynamic parameters, allowing users to build customized simulation environments.

- Additional libraries support higher-level operations such as motion and task planning.

- **ROS 2**: the [ROS 2 driver](../ros2/index.md) connects the robot to ROS 2 and MoveIt 2 through the same gRPC interface.

- **Web UI**: a browser interface on the RPC for status, power, servos and settings. See [Web UI](web-ui.md).

---
## Models

The SDK offers **URDF** and **MJCF** (MuJoCo) files for each model and hardware version, which allow users to perform simulations without physical hardware.
These models enable testing of robot movements and strategies in a virtual environment.

::: info Note
The models are in the `models` folder of rby1-sdk. See [Robot Models](../sdk/models/index.md) and [Hardware Versions](../sdk/models/hardware-versions.md)
to find the file for your robot, and [Units and Frames](units-and-frames.md) for the frames and link names.
:::

---
## Simulation Tools

The robot software also runs in simulation: a MuJoCo-based simulator (Docker image) and an Isaac Sim setup.
Both serve the same gRPC interface as the robot, so SDK programs run unchanged.
See [Simulation](../simulators/index.md) for the images, tags and requirements.

---

## Actuator List and Robot State Data

<img :src="$withBase('/images/software/architecture/hardware-overview.png')" alt="hardware-overview" class="center white-bg" style="width:600px">

`RobotState.position` (and the other per-joint arrays of the robot state) has one value per joint, in the joint order of the model.
For Model A this is 24 joints:

- right_wheel, left_wheel
- torso_0 to torso_5
- right_arm_0 to right_arm_6
- left_arm_0 to left_arm_6
- head_0, head_1

Model M has four wheels (26 joints) and Model UB has no wheels and a two-joint torso (18 joints).
The order of each model is in [Units and Frames](units-and-frames.md#joint-order) and on the [model pages](../sdk/models/index.md).
In code, read it with `robot.model().robot_joint_names`.

The **torso actuators (torso_0 to torso_5)** are listed from bottom to top, while the arm actuators (right_arm, left_arm) are ordered from shoulder to wrist.

For all fields of the robot state, see the [RobotState proto](../sdk/protos/generated/robot_state/robotstate.md) and the
SDK example `03_robot_state.py`.

<img :src="$withBase('/images/software/architecture/actuator-list.png')" alt="actuator-list" class="center white-bg" style="width:600px">

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/model.h` (joint order of A, M, UB), `include/rby1-sdk/robot_state.h`,
`models/` (URDF and MuJoCo files per version), `examples/python/03_robot_state.py`; robot core `core/main.cpp` (gRPC port 50051),
`core/control/impl/rt.h` (real-time control).
