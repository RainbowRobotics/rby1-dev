# Overview

`rby1_ros2` is the ROS 2 driver of the Rainbow Robotics RB-Y1.
It wraps the RB-Y1 C++ SDK in a ROS 2 node that publishes the robot state and takes commands (joint position, Cartesian position, impedance, gravity compensation, command streams and trajectories) as topics, services and actions.
It also has a `ros2_control` hardware plugin, MoveIt 2 configurations and a planner, the robot description, examples and tools.

- **Driver version**: rby1-ros2 v1.0.0 ([RainbowRobotics/rby1-ros2](https://github.com/RainbowRobotics/rby1-ros2))
- **ROS 2 version**: Humble on Ubuntu 22.04 (recommended), Jazzy on Ubuntu 24.04
- **SDK compatibility**: rby1-sdk `0.10.x` and later, the C++ SDK built from source
- **Robots**: RB-Y1 Model A v1.0, v1.1, v1.2 and Model M v1.0, v1.1, v1.2, v1.3, and the simulator with the same model and version. Model UB is not supported (the driver's `model` takes only `a` or `m`).

::: danger Test in a simulator first
The driver, the examples and MoveIt move the real robot. Before you run anything on a robot:
- Test the same commands in the [simulator](../../simulators/mujoco.md) first.
- Keep the E-Stop within reach.
- Clear the reach of the arms and torso, and the driving path of the base.
:::

To install and build the packages, see [Install & Build](install_and_build.md).

<img :src="$withBase('/images/ros2/system_architecture.png')" alt="RB-Y1 ROS 2 driver system architecture" class="center" style="width:100%">

Two paths lead to the robot. The robot takes commands from one owner at a time.
1. **The driver (`rby1_ros2_driver`)**: a C++ node connected to the robot or the simulator over gRPC. It publishes the robot state at 100 Hz and takes commands as services and actions (e.g. `robot_joint`, `robot_cartesian`), plus `cmd_vel` for the base. The examples, the [MoveIt planner](moveit_planner.md) and the tools all go through it.
2. **The `ros2_control` hardware plugin (`rby1_hardware`)**: loaded by a `ros2_control` controller manager, under MoveIt (`demo.launch.py` of a `rby1_moveit_*` package) or alone ([ros2_control Hardware Interface](hardware_interface.md)). It streams joint positions to the robot over its own gRPC connection, and asks the running driver for power, servos and the control right (`/rby1/hardware_control`). While it holds the control right, the driver refuses its own command sources.

The packages are listed in [Package Architecture](package_architecture.md).

## Namespace

The driver launch file starts the node in the namespace `rby1` (launch argument `namespace`), so all topics, services and actions
on these pages are under `/rby1/`, for example `/rby1/stream_control` and `/rby1/joint_states`.
Check the node name after launch:

```bash
ros2 node list    # /rby1/rby1_ros2_driver
```

To use another namespace, start the driver with `namespace:=<name>`, and use the same name in your commands
(and in `driver_namespace` for MoveIt, see [MoveIt 2](rby1_moveit2.md)).

Verified against: rby1-ros2 v1.0.0 `README.md`, `Doc/manual/01_overview.md`, `rby1_driver/src/main.cpp`, `rby1_driver/launch/rby1_ros2_driver.launch.py`.
