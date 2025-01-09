---
title: Software Stack
outline: deep
---

# Software Architecture

## System Overview

> :warning: **Note:** Future updates to the SDK will include official support for **ROS** integration, as well as **SLAM** and **Navigation** modules for autonomous operation. These features are currently in development and will be available in a future release.


The software architecture ensures stable performance and safety while providing scalability for the robot. It is designed to cover various application needs and enables quick and efficient development of custom solutions through its scalable structure.

<figure>
    <img src="/images/rby-software-stack-white.png" alt="missing" style="margin:auto;" />
    <figcaption style="text-align: center;">[ Software architecture of RB-Y1 ]</figcaption>
</figure>

This architecture is composed as follows:

- **Independent robot internal controllers (Robot PC)**: Ensures stable performance and safety. It operates alongside the application control PC (**User PC**) to offer scalability.
- **Non-realtime communication channels**: Designed for high-level commands and robot settings, such as power management. These channels use **Google gRPC**, allowing commands to be built using a **builder pattern** and executed at **up to 100Hz**. Two types of communication patterns are available:
    1. **Once**: Suitable for executing a single command at a time, such as setting a target position or velocity. This method is used for one-time commands that do not require continuous updates.
    2. **Stream**: Designed for continuous command exchange, ideal for tasks where frequent updates are necessary. If you need to send and receive commands regularly, **Stream** mode is recommended for maintaining smooth operations.
    
    Available controllers include:
    - Joint Position Control
    - Joint Velocity Control
    - Cartesian Control
    - Gravity Compensation Control
    - Optimal Control
    - Impedance Control
    - SE2 Velocity Control
- **Realtime command channels**: Focused on low-level, time-sensitive commands with responses at **500Hz** using **UDP**. While currently fixed at 500Hz, future updates will allow for variable frequencies. Users can implement their own position or torque controllers for real-time operations.
- A **robot model library**: Provides access to the robot's kinematic and dynamic parameters, allowing users to build customized simulation environments.
- Additional libraries support higher-level operations such as motion and task planning.

## Models

The SDK currently offers **URDF** and **MJCF** files, which allow users to perform simulations without physical hardware. These models enable testing of robot movements and strategies in a virtual environment.

> :warning: **Note:** These models are included in the SDK, and detailed setup instructions are available in the documentation.

## Simulation Tools

A **MuJoCo-based simulator** for the Rainbow Robotics RBY series is now publicly available on **Docker Hub**. This simulator provides comprehensive simulation capabilities in realistic environments, accessible in both ARM and x86 architectures.

- **Docker Images:**
  - ARM version: [rainbowroboticsofficial/rby1-sim-arm](https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim-arm)
  - x86 version: [rainbowroboticsofficial/rby1-sim](https://hub.docker.com/r/rainbowroboticsofficial/rby1-sim)

> ⚠️ **Note:** X11 forwarding (`xhost+`) is required for the GUI. Lower-spec devices may experience performance limitations. Although profiling hasn't been conducted, it is recommended to use a system with at least **Intel i5** or equivalent CPU and **16GB RAM** for optimal performance.

## Actuator List and Robot State Data
<figure style="text-align: center">
    <img src="/images/hardware-overview.png" alt="missing" style="width:100%;margin:auto;" />
</figure>

The **RobotState/position** provides position data for all 24 actuators in the robot, processed in the following order:

- right_wheel, left_wheel
- torso_0 to torso_5
- right_arm_0 to right_arm_6
- left_arm_0 to left_arm_6
- head_0, head_1

The **torso actuators (torso_0 to torso_5)** are listed from bottom to top, while the **arm actuators** (right_arm, left_arm) are ordered from shoulder to wrist.

For more detailed information about **RobotState**, please refer to the [RobotState section on this site](https://rainbowrobotics.github.io/rby1-dev/docs/development/rby1-sdk/protos.html#robotstate).


<figure style="text-align: center"> 
    <img src="/images/actuator-list.png" alt="Actuator List" style="width:100%;margin:auto;" /> 
</figure>

