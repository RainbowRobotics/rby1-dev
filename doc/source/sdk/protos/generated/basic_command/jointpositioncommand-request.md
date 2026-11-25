(rb-api-jointpositioncommand-request)=
# JointPositionCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for JointPositionCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| position | [double](../scalar-value-types.md) | repeated |  |
| velocity_limit | [double](../scalar-value-types.md) | repeated |  |
| acceleration_limit | [double](../scalar-value-types.md) | repeated |  |
