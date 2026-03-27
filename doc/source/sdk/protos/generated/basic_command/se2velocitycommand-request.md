# SE2VelocityCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for SE2VelocityCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| velocity | [SE2Velocity](../geometry/se2velocity.md#rb-api-se2velocity) |  |  |
| acceleration_limit | [SE2Velocity](../geometry/se2velocity.md#rb-api-se2velocity) |  |  |
