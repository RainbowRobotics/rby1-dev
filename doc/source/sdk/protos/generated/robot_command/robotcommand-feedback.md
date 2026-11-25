(rb-api-robotcommand-feedback)=
# RobotCommand.Feedback

- Source proto: `rb/api/robot_command.proto`

Feedback payload for RobotCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| whole_body_command_feedback | [WholeBodyCommand.Feedback](../whole_body_command/wholebodycommand-feedback.md) |  |  |
| component_based_command_feedback | [ComponentBasedCommand.Feedback](../component_based_command/componentbasedcommand-feedback.md) |  |  |
| jog_command_feedback | [JogCommand.Feedback](../basic_command/jogcommand-feedback.md) |  |  |
| status | [RobotCommand.Feedback.Status](robotcommand-feedback-status.md) |  |  |
| finish_code | [RobotCommand.Feedback.FinishCode](robotcommand-feedback-finishcode.md) |  |  |
