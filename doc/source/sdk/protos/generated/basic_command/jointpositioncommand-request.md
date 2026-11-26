(rb-api-jointpositioncommand-request)=
# JointPositionCommand.Request

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Request part of [JointPositionCommand](jointpositioncommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| position | [double](../scalar-value-types.md) | repeated |  |
| velocity_limit | [double](../scalar-value-types.md) | repeated |  |
| acceleration_limit | [double](../scalar-value-types.md) | repeated |  |
