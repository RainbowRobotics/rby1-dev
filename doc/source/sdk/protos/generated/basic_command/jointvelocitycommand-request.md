# JointVelocityCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for JointVelocityCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| velocity | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| acceleration_limit | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
