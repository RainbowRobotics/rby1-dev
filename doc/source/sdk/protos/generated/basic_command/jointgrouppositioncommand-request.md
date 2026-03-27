# JointGroupPositionCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for JointGroupPositionCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| joint_names | [string](../scalar-value-types.md#scalar-value-types) | repeated |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| position | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| velocity_limit | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| acceleration_limit | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
