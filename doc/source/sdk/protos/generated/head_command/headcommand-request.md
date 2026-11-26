(rb-api-headcommand-request)=
# HeadCommand.Request

- Source proto: [`rb/api/head_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/head_command.proto) (rby1-sdk v0.10.1)

Request part of [HeadCommand](headcommand.md).

Only one field of the `command` oneof can be set at a time: `joint_position_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md) | oneof command |  |
