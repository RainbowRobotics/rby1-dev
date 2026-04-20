(rb-api-se2velocitycommand-request)=
# SE2VelocityCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for SE2VelocityCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| velocity | [SE2Velocity](../geometry/se2velocity.md) |  |  |
| acceleration_limit | [SE2Velocity](../geometry/se2velocity.md) |  |  |
