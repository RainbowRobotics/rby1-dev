(rb-api-jointstate)=
# JointState

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

State of one joint: status flags, position, velocity, current, torque, the last target and the motor temperature.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| is_ready | [bool](../scalar-value-types.md) |  |  |
| fet_state | [JointState.FETState](jointstate-fetstate.md) |  |  |
| run_state | [JointState.RunState](jointstate-runstate.md) |  |  |
| init_state | [JointState.InitializationState](jointstate-initializationstate.md) |  |  |
| motor_type | [uint32](../scalar-value-types.md) |  |  |
| motor_state | [uint64](../scalar-value-types.md) |  |  |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| power_on | [bool](../scalar-value-types.md) |  |  |
| position | [double](../scalar-value-types.md) |  | Joint position (rad). |
| velocity | [double](../scalar-value-types.md) |  | Joint velocity (rad/s). |
| current | [double](../scalar-value-types.md) |  | Motor current (A). |
| torque | [double](../scalar-value-types.md) |  | Joint torque (Nm). |
| target_position | [double](../scalar-value-types.md) |  | Position of the last target (rad). |
| target_velocity | [double](../scalar-value-types.md) |  | Velocity of the last target (rad/s). |
| target_feedback_gain | [uint32](../scalar-value-types.md) |  | Feedback gain of the last target, 0 to 10. |
| target_feedforward_torque | [double](../scalar-value-types.md) |  | Feedforward torque of the last target (Nm). |
| temperature | [int32](../scalar-value-types.md) |  | Motor temperature (°C). |
