# JogCommand.Request

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](./commandheader-request.md#rb-api-commandheader-request) |  |  |
| joint_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) (optional) |
| acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s^2) (optional) |
| absolute_position | [double](./scalar-value-types.md#scalar-value-types) |  | (rad) |
| relative_position | [double](./scalar-value-types.md#scalar-value-types) |  | (rad) current position &#43; relative position |
| one_step | [bool](./scalar-value-types.md#scalar-value-types) |  | 5 deg, true is positive move, false is negative move |
