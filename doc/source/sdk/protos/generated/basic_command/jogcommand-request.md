# JogCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for JogCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| joint_name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| velocity_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (rad/s) (optional) |
| acceleration_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (rad/s^2) (optional) |
| absolute_position | [double](../scalar-value-types.md#scalar-value-types) |  | (rad) |
| relative_position | [double](../scalar-value-types.md#scalar-value-types) |  | (rad) current position &#43; relative position |
| one_step | [bool](../scalar-value-types.md#scalar-value-types) |  | 5 deg, true is positive move, false is negative move |
