(rb-api-robotstate)=
# RobotState

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

Full state of the robot at one time: system, battery, power, EMO, joint and sensor states, odometry, center of mass and collisions. Arrays with one value per joint use the robot joint order (see RobotInfo).

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
| position | [double](../scalar-value-types.md) | repeated | Joint positions (rad), one per joint. |
| velocity | [double](../scalar-value-types.md) | repeated | Joint velocities (rad/s), one per joint. |
| current | [double](../scalar-value-types.md) | repeated | Motor currents (A), one per joint. |
| torque | [double](../scalar-value-types.md) | repeated | Joint torques (Nm), one per joint. |
| target_position | [double](../scalar-value-types.md) | repeated | Positions of the last target (rad), one per joint. |
| target_velocity | [double](../scalar-value-types.md) | repeated | Velocities of the last target (rad/s), one per joint. |
| target_feedback_gain | [uint32](../scalar-value-types.md) | repeated |  |
| target_feedforward_torque | [double](../scalar-value-types.md) | repeated | Feedforward torques of the last target (Nm), one per joint. |
| odometry | [SE2Pose](../geometry/se2pose.md) |  | Mobility State |
| center_of_mass | [Vec3](../geometry/vec3.md) |  | Center of mass position with respect to the base link. |
| collisions | [Collision](collision.md) | repeated | Link pairs that are close to each other or in collision. |
| temperature | [int32](../scalar-value-types.md) | repeated | Motor temperatures (°C), one per joint. |
