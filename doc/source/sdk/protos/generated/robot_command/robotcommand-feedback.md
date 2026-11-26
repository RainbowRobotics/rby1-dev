(rb-api-robotcommand-feedback)=
# RobotCommand.Feedback

- Source proto: [`rb/api/robot_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_command.proto) (rby1-sdk v0.10.1)

Feedback part of [RobotCommand](robotcommand.md).

Only one field of the `feedback` oneof can be set at a time: `whole_body_command_feedback`, `component_based_command_feedback`, `jog_command_feedback`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| whole_body_command_feedback | [WholeBodyCommand.Feedback](../whole_body_command/wholebodycommand-feedback.md) | oneof feedback |  |
| component_based_command_feedback | [ComponentBasedCommand.Feedback](../component_based_command/componentbasedcommand-feedback.md) | oneof feedback |  |
| jog_command_feedback | [JogCommand.Feedback](../basic_command/jogcommand-feedback.md) | oneof feedback |  |
| status | [RobotCommand.Feedback.Status](robotcommand-feedback-status.md) |  |  |
| finish_code | [RobotCommand.Feedback.FinishCode](robotcommand-feedback-finishcode.md) |  |  |
