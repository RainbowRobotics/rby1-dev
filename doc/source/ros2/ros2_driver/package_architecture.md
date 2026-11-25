# Package Architecture

## System Architecture

The RBY1 ROS 2 package supports both direct control (via stand-alone services, actions, and topics in the `rby1_ros2_driver` C++ node) and MoveIt 2 motion planning (via the standard `ros2_control` pipeline and `rby1_hardware::RBY1SystemHardware` system interface).

## Package Structure

| Package | Role |
|---------|------|
| `rby1_driver` | C++ main driver node. Wraps the RBY1 SDK and exposes a ROS 2 interface. |
| `rby1_msgs` | Custom message, service, and action definitions for robot control and state. |
| `rby1_examples` | Python example scripts demonstrating all major driver features. |
| `rby1_description` | Robot description for ROS, demonstrating URDF and Mesh files, and simple visualization launch file. |
| `rby1_hardware` | `ros2_control` SystemInterface plugin (`RBY1SystemHardware`). Bridges the RBY1 SDK to MoveIt 2 via the standard `ros2_control` hardware interface pipeline. |
| `rby1_moveit_a_1_0` | MoveIt 2 configuration package for **Model A v1.0** (SRDF, controllers, kinematics, joint limits). |
| `rby1_moveit_a_1_1` | MoveIt 2 configuration package for **Model A v1.1**. |
| `rby1_moveit_a_1_2` | MoveIt 2 configuration package for **Model A v1.2**. |
| `rby1_moveit_m_1_0` | MoveIt 2 configuration package for **Model M v1.0**. |
| `rby1_moveit_m_1_1` | MoveIt 2 configuration package for **Model M v1.1**. |
| `rby1_moveit_m_1_2` | MoveIt 2 configuration package for **Model M v1.2**. |
| `rby1_moveit_m_1_3` | MoveIt 2 configuration package for **Model M v1.3**. |

### Sequence & Architecture Flow (Mermaid Diagram)

```{mermaid}
graph TD
    subgraph user_space ["User Space"]
        UserNode[User Node / Examples]
        MoveIt[MoveIt 2 / MoveGroup]
    end

    subgraph driver_control ["ROS 2 Control & Driver Layer"]
        subgraph driver ["rby1_ros2_driver C++ Node"]
            DriverState[State Publisher]
            DriverSrv[Service Handlers]
            DriverAction[Action Servers]
        end

        subgraph control ["ros2_control Controller Manager"]
            Controllers[JointTrajectory & Gripper Controllers]
            HWInterface[rby1_hardware::RBY1SystemHardware]
        end
    end

    subgraph robot_layer ["Robot / Simulation Layer"]
        Robot[RBY1 Robot / Sim]
    end

    %% Connections
    UserNode -->|Subscribe State| DriverState
    UserNode -->|Call Services| DriverSrv
    UserNode -->|Send Actions| DriverAction
    
    MoveIt -->|Send Trajectory| Controllers
    Controllers -->|Read State / Write Command| HWInterface

    %% Coordination
    HWInterface -->|Claim Control / Power / Servo| DriverSrv

    %% gRPC Connections
    DriverState -->|gRPC| Robot
    DriverSrv -->|gRPC| Robot
    DriverAction -->|gRPC| Robot
    HWInterface -->|gRPC Direct Stream| Robot

    classDef pkg fill:#1e293b,stroke:#475569,stroke-width:2px,color:#f8fafc;
    classDef comp fill:#334155,stroke:#64748b,stroke-width:1px,color:#f8fafc;
    classDef robot fill:#14532d,stroke:#15803d,stroke-width:2px,color:#f8fafc;
    
    class MoveIt,UserNode pkg;
    class DriverState,DriverSrv,DriverAction,Controllers,HWInterface comp;
    class Robot robot;
```
