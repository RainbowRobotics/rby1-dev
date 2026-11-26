# Topics

All topic names are relative to the driver's namespace, `rby1` by default (for example, `/rby1/joint_states`).
See [Overview](overview.md#namespace).

## Publishers
| Topic | Type | Always Active | Description |
|-------|------|:---:|-------------|
| `joint_overall_states` | `sensor_msgs/JointState` | ✅ | State of every joint, including the wheels. This is the topic that TF, MoveIt and RViz read. |
| `joint_states` | `rby1_msgs/PartJointStates` | ✅ | Joint state per part (`torso`, `right_arm`, `left_arm`, `head`), for monitoring and logging. See [Custom Message Types](custom_message_types.md). |
| `robot_state` | `rby1_msgs/RobotState` | ✅ | Control Manager state, brakes, EMO, CoM, stream, collision |
| `battery_state` | `sensor_msgs/BatteryState` | ⚙️ `publish_battery_state` | Battery voltage, current, percentage |
| `tool_flange/left/imu`, `tool_flange/right/imu` | `sensor_msgs/Imu` | ⚙️ `publish_tool_flange_state` | Tool flange IMU |
| `tool_flange/left/wrench`, `tool_flange/right/wrench` | `geometry_msgs/WrenchStamped` | ⚙️ `publish_tool_flange_state` | Tool flange force/torque sensor |
| `odom` | `nav_msgs/Odometry` | ✅ | High-rate robot odometry and TF broadcast relative to node namespace |

::: info Note
Since rby1-ros2 v1.0.0, `joint_states` is `rby1_msgs/PartJointStates`, no longer `sensor_msgs/JointState`,
and the per-part topics `joint_states/torso`, `joint_states/right_arm`, `joint_states/left_arm` and `joint_states/head` are removed.
Subscribe to `joint_overall_states` if your node expects `sensor_msgs/JointState`.
:::

## Subscribers

| Topic | Type | Description |
|-------|------|-------------|
| `cmd_vel` | `geometry_msgs/Twist` | Velocity command for driving base wheels (linear x, y and angular z) |

::: warning Important
**Mobile base control (`cmd_vel`) needs the command stream.**
Since `cmd_vel` acts as a high-frequency publisher, you must enable persistent stream control before publishing base velocity commands.
- Call `/rby1/stream_control` with `state: true` before sending `cmd_vel` commands.
- Call `/rby1/stream_control` with `state: false` after finishing base control to return to regular position hold.
- Activating `/rby1/stream_control` when it is already active is idempotent; the service logs a warning and returns success.
:::
