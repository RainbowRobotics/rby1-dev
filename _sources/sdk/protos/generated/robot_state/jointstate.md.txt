# JointState

- Source proto: `rb/api/robot_state.proto`

State snapshot for joint.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_ready | [bool](../scalar-value-types.md#scalar-value-types) |  |  |
| fet_state | [JointState.FETState](jointstate-fetstate.md#rb-api-jointstate-fetstate) |  |  |
| run_state | [JointState.RunState](jointstate-runstate.md#rb-api-jointstate-runstate) |  |  |
| init_state | [JointState.InitializationState](jointstate-initializationstate.md#rb-api-jointstate-initializationstate) |  |  |
| motor_type | [uint32](../scalar-value-types.md#scalar-value-types) |  | MOTOR STATE |
| motor_state | [uint64](../scalar-value-types.md#scalar-value-types) |  |  |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| power_on | [bool](../scalar-value-types.md#scalar-value-types) |  |  |
| position | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| velocity | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| current | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| torque | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| target_position | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| target_velocity | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| target_feedback_gain | [uint32](../scalar-value-types.md#scalar-value-types) |  |  |
| target_feedforward_torque | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| temperature | [int32](../scalar-value-types.md#scalar-value-types) |  |  |
