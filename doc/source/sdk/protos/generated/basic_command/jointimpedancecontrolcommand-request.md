(rb-api-jointimpedancecontrolcommand-request)=
# JointImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for JointImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| position | [double](../scalar-value-types.md) | repeated |  |
| velocity_limit | [double](../scalar-value-types.md) | repeated |  |
| acceleration_limit | [double](../scalar-value-types.md) | repeated |  |
| stiffness | [double](../scalar-value-types.md) | repeated |  |
| damping_ratio | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1 |
| torque_limit | [double](../scalar-value-types.md) | repeated |  |
