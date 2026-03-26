# JointImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](./commandheader-request.md#rb-api-commandheader-request) |  |  |
| minimum_time | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| position | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
| velocity_limit | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
| acceleration_limit | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
| stiffness | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
| damping_ratio | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1 |
| torque_limit | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
