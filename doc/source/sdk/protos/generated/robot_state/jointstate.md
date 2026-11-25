(rb-api-jointstate)=
# JointState

- Source proto: `rb/api/robot_state.proto`

State snapshot for joint.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_ready | [bool](../scalar-value-types.md) |  |  |
| fet_state | [JointState.FETState](jointstate-fetstate.md) |  |  |
| run_state | [JointState.RunState](jointstate-runstate.md) |  |  |
| init_state | [JointState.InitializationState](jointstate-initializationstate.md) |  |  |
| motor_type | [uint32](../scalar-value-types.md) |  | MOTOR STATE |
| motor_state | [uint64](../scalar-value-types.md) |  |  |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| power_on | [bool](../scalar-value-types.md) |  |  |
| position | [double](../scalar-value-types.md) |  |  |
| velocity | [double](../scalar-value-types.md) |  |  |
| current | [double](../scalar-value-types.md) |  |  |
| torque | [double](../scalar-value-types.md) |  |  |
| target_position | [double](../scalar-value-types.md) |  |  |
| target_velocity | [double](../scalar-value-types.md) |  |  |
| target_feedback_gain | [uint32](../scalar-value-types.md) |  |  |
| target_feedforward_torque | [double](../scalar-value-types.md) |  |  |
| temperature | [int32](../scalar-value-types.md) |  |  |
