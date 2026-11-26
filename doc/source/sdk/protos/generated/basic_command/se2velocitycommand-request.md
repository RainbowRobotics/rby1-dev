(rb-api-se2velocitycommand-request)=
# SE2VelocityCommand.Request

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Request part of [SE2VelocityCommand](se2velocitycommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| velocity | [SE2Velocity](../geometry/se2velocity.md) |  |  |
| acceleration_limit | [SE2Velocity](../geometry/se2velocity.md) |  |  |
