# Topics

All topic names are relative to the driver's namespace, `rby1` by default (for example, `/rby1/joint_states`).
See [Overview](overview.md#namespace).

## Publishers
| Topic | Type | Published | Description |
|-------|------|:---:|-------------|
| `joint_overall_states` | `sensor_msgs/JointState` | ✅ | State of every joint, including the wheels. This is the topic that TF, MoveIt and RViz read. |
| `joint_states` | `rby1_msgs/PartJointStates` | ✅ | Joint state per part (`torso`, `right_arm`, `left_arm`, `head`), for monitoring and logging. See [Custom Message Types](custom_message_types.md). |
| `robot_state` | `rby1_msgs/RobotState` | ✅ | Control Manager state, brakes, tool flanges, E-Stop, centre of mass, stream open, collision |
| `battery_state` | `sensor_msgs/BatteryState` | ⚙️ `publish_battery_state` | Battery voltage, current, percentage |
| `tool_flange/left/imu`, `tool_flange/right/imu` | `sensor_msgs/Imu` | ⚙️ `publish_tool_flange_state` | Tool flange IMU |
| `tool_flange/left/wrench`, `tool_flange/right/wrench` | `geometry_msgs/WrenchStamped` | ⚙️ `publish_tool_flange_state` | Tool flange force/torque sensor |
| `odom` | `nav_msgs/Odometry` | ✅ | Robot odometry, and TF `odom → base_footprint` |

✅ = always published. ⚙️ = published when the named flag in [`driver_parameters.yaml`](config_driver_parameters.md) is `true`.

::: info Note
Since rby1-ros2 v1.0.0, `joint_states` is `rby1_msgs/PartJointStates`, no longer `sensor_msgs/JointState`,
and the per-part topics `joint_states/torso`, `joint_states/right_arm`, `joint_states/left_arm` and `joint_states/head` are removed.
Subscribe to `joint_overall_states` if your node expects `sensor_msgs/JointState`.
:::

In the simulator, battery, force/torque and IMU values read 0.

## Subscribers

| Topic | Type | Description |
|-------|------|-------------|
| `cmd_vel` | `geometry_msgs/Twist` | Velocity command for the mobile base (linear x, y and angular z). Needs the `mobile` stream channel open |

::: danger Mobile base control (`cmd_vel`) moves the robot
Clear the driving path and keep the E-Stop within reach before you publish `cmd_vel`. Try it in the simulator first.

- Open the `mobile` channel first. The driver ignores `cmd_vel` while it is closed:
  ```bash
  ros2 service call /rby1/stream_control rby1_msgs/srv/StateOnOff "{state: true, parameters: 'mobile'}"
  ```
- Each message is carried out for 1.1 × 1/`stream_command_hz` (about 37 ms at the default 30 Hz), so publish at that rate.
- The driver sets a control hold time of 1 s on each velocity command. Under the SDK's [control hold time](../../sdk/controllers/generated/control_hold_time_and_minimum_time.md) rule,
  the base can keep moving at the last velocity for up to that long after the last message, for example when your node crashes.
  To stop, publish a zero velocity first, then stop publishing.
- Close the channel when you are done: `{state: false, parameters: 'mobile'}`. Opening a channel that is already open is not an error.
:::

See [Command Streams](command_streams.md) for how the channels work.
