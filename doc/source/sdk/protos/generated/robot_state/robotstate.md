# RobotState

- Source proto: `rb/api/robot_state.proto`

State snapshot for robot.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| system_stat | [SystemStat](systemstat.md#rb-api-systemstat) |  | System Statistic |
| battery_state | [BatteryState](batterystate.md#rb-api-batterystate) |  | Battery State |
| power_states | [PowerState](powerstate.md#rb-api-powerstate) | repeated | Power State |
| emo_states | [EMOState](emostate.md#rb-api-emostate) | repeated | EMO state |
| joint_states | [JointState](jointstate.md#rb-api-jointstate) | repeated | Joint State |
| tool_flange_right | [ToolFlangeState](toolflangestate.md#rb-api-toolflangestate) |  | Tool Flange State |
| tool_flange_left | [ToolFlangeState](toolflangestate.md#rb-api-toolflangestate) |  |  |
| ft_sensor_right | [FTSensorData](ftsensordata.md#rb-api-ftsensordata) |  | Force Torque Sensor |
| ft_sensor_left | [FTSensorData](ftsensordata.md#rb-api-ftsensordata) |  |  |
| is_ready | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| position | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| velocity | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| current | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| torque | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| target_position | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| target_velocity | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| target_feedback_gain | [uint32](../scalar-value-types.md#scalar-value-types) | repeated |  |
| target_feedforward_torque | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| odometry | [SE2Pose](../geometry/se2pose.md#rb-api-se2pose) |  | Mobility State |
| center_of_mass | [Vec3](../geometry/vec3.md#rb-api-vec3) |  | Center Of Mass

Position of center of mass with respect t base link |
| collisions | [Collision](collision.md#rb-api-collision) | repeated | Collisions |
| temperature | [int32](../scalar-value-types.md#scalar-value-types) | repeated | Temperature |
