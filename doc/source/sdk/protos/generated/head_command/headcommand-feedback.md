(rb-api-headcommand-feedback)=
# HeadCommand.Feedback

- Source proto: [`rb/api/head_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/head_command.proto) (rby1-sdk v0.10.1)

Feedback part of [HeadCommand](headcommand.md).

Only one field of the `feedback` oneof can be set at a time: `joint_position_command_feedback`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](../basic_command/jointpositioncommand-feedback.md) | oneof feedback |  |
