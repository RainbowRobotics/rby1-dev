# Overview

`rby1_ros2` is a unified ROS 2 driver package for controlling the Rainbow Robotics RBY1 robot.  
It wraps the RBY1 C++ SDK into a ROS 2 node, providing state monitoring and multiple control modes (Joint Position, Cartesian Position, Impedance, Gravity Compensation, and Trajectory Streaming) through a clean action/service/topic interface.

- **Driver version**: rby1-ros2 v1.0.0 ([RainbowRobotics/rby1-ros2](https://github.com/RainbowRobotics/rby1-ros2))
- **ROS 2 version**: Humble (recommended), Jazzy
- **OS**: Ubuntu 22.04, 24.04
- **SDK compatibility**: rby1-sdk `0.10.x` and later

To install and build the packages, see [Install & Build](install_and_build.md).

```{image} ../../_static/images/ros2/system_architecture.png
    :width: 100%
    :align: center
```

The system operates using two primary pipelines to interface with the robot:
1. **Direct Control Mode (`rby1_ros2_driver`)**: A standalone C++ ROS 2 node that communicates directly with the RBY1 robot or simulator via gRPC. User applications/scripts send standard ROS 2 topics, services, and actions (e.g. `robot_joint`, `robot_cartesian`) to command movements and monitor status.
2. **MoveIt 2 Integration (`rby1_hardware`)**: Bridges MoveIt 2 and `ros2_control` to the robot via a custom `RBY1SystemHardware` interface plugin. The hardware plugin streams command inputs to the robot via a direct gRPC connection, while querying status and coordinating power, servo states, and control rights with the `rby1_ros2_driver` node via internal ROS 2 service calls (like `/rby1/hardware_control`).

## Namespace

The driver launch file starts the node in the namespace `rby1` (launch argument `namespace`), so all topics, services and actions
on these pages are under `/rby1/`, for example `/rby1/stream_control` and `/rby1/joint_states`.
Check the node name after launch:

```bash
ros2 node list    # /rby1/rby1_ros2_driver
```

To use another namespace, start the driver with `namespace:=<name>`, and use the same name in your commands
(and in `driver_namespace` for MoveIt, see [RBY1 MoveIt2](rby1_moveit2.md)).
