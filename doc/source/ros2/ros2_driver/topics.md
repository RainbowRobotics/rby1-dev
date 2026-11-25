# Topics 

## Publishers
| Topic | Type | Always Active | Description |
|-------|------|:---:|-------------|
| `joint_states` | `sensor_msgs/JointState` | ✅ | Consolidated state of all joints of the robot |
| `joint_states/torso` | `sensor_msgs/JointState` | ✅ | Torso joint positions, velocities, torques |
| `joint_states/right_arm` | `sensor_msgs/JointState` | ✅ | Right arm joint state |
| `joint_states/left_arm` | `sensor_msgs/JointState` | ✅ | Left arm joint state |
| `joint_states/head` | `sensor_msgs/JointState` | ✅ | Head joint state |
| `robot_state` | `rby1_msgs/RobotState` | ✅ | Control Manager state, brakes, EMO, CoM, stream, collision |
| `battery_state` | `sensor_msgs/BatteryState` | ⚙️ `publish_battery_state` | Battery voltage, current, percentage |
| `tool_flange/left` | `rby1_msgs/ToolFlangeState` | ⚙️ `publish_tool_flange_state` | Left flange: FT sensor, IMU, switch, voltage, digital I/O |
| `tool_flange/right` | `rby1_msgs/ToolFlangeState` | ⚙️ `publish_tool_flange_state` | Right flange: FT sensor, IMU, switch, voltage, digital I/O |
| `odom` | `nav_msgs/Odometry` | ✅ | High-rate robot odometry and TF broadcast relative to node namespace |

## Subscribers

| Topic | Type | Description |
|-------|------|-------------|
| `cmd_vel` | `geometry_msgs/Twist` | Velocity command for driving base wheels (linear x, y and angular z) |

> [!IMPORTANT]
> **Mobile Base Control (`cmd_vel`) streaming requirement:**
> Since `cmd_vel` acts as a high-frequency publisher, **you must enable persistent stream control** before publishing base velocity commands.
> - Call `/stream_control` with `state: true` before sending `cmd_vel` commands.
> - Call `/stream_control` with `state: false` after finishing base control to return to regular position hold.
> - Attempting to activate `/stream_control` when already active is idempotent; the service will safely log a warning and return success.


