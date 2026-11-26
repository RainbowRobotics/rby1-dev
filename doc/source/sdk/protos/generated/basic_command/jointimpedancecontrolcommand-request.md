(rb-api-jointimpedancecontrolcommand-request)=
# JointImpedanceControlCommand.Request

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Request part of [JointImpedanceControlCommand](jointimpedancecontrolcommand.md).

See also: [Control Hold Time and Minimum Time](../../../controllers/generated/control_hold_time_and_minimum_time.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  | Minimum time to reach the target. |
| position | [double](../scalar-value-types.md) | repeated | Target joint positions (rad). One value per joint of the component, in its joint order. |
| velocity_limit | [double](../scalar-value-types.md) | repeated | Joint velocity limits (rad/s), one per joint. Leave empty to use the defaults. |
| acceleration_limit | [double](../scalar-value-types.md) | repeated | Joint acceleration limits (rad/s²), one per joint. Leave empty to use the defaults. |
| stiffness | [double](../scalar-value-types.md) | repeated | Joint stiffness (Nm/rad), one per joint. Must not be negative. |
| damping_ratio | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1 |
| torque_limit | [double](../scalar-value-types.md) | repeated | Limit of the commanded joint torque (Nm), one per joint. Leave empty to use the defaults. |
