(rb-api-robotstate)=
# RobotState

- Source proto: `rb/api/robot_state.proto`

State snapshot for robot.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| system_stat | [SystemStat](systemstat.md) |  | System Statistic |
| battery_state | [BatteryState](batterystate.md) |  | Battery State |
| power_states | [PowerState](powerstate.md) | repeated | Power State |
| emo_states | [EMOState](emostate.md) | repeated | EMO state |
| joint_states | [JointState](jointstate.md) | repeated | Joint State |
| tool_flange_right | [ToolFlangeState](toolflangestate.md) |  | Tool Flange State |
| tool_flange_left | [ToolFlangeState](toolflangestate.md) |  |  |
| ft_sensor_right | [FTSensorData](ftsensordata.md) |  | Force Torque Sensor |
| ft_sensor_left | [FTSensorData](ftsensordata.md) |  |  |
| is_ready | [double](../scalar-value-types.md) | repeated |  |
| position | [double](../scalar-value-types.md) | repeated |  |
| velocity | [double](../scalar-value-types.md) | repeated |  |
| current | [double](../scalar-value-types.md) | repeated |  |
| torque | [double](../scalar-value-types.md) | repeated |  |
| target_position | [double](../scalar-value-types.md) | repeated |  |
| target_velocity | [double](../scalar-value-types.md) | repeated |  |
| target_feedback_gain | [uint32](../scalar-value-types.md) | repeated |  |
| target_feedforward_torque | [double](../scalar-value-types.md) | repeated |  |
| odometry | [SE2Pose](../geometry/se2pose.md) |  | Mobility State |
| center_of_mass | [Vec3](../geometry/vec3.md) |  | Center Of Mass

Position of center of mass with respect t base link |
| collisions | [Collision](collision.md) | repeated | Collisions |
| temperature | [int32](../scalar-value-types.md) | repeated | Temperature |
