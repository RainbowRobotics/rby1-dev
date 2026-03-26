# RobotCommand.Feedback

- Source proto: `rb/api/robot_command.proto`

Feedback payload for RobotCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| whole_body_command_feedback | [WholeBodyCommand.Feedback](../whole_body_command/wholebodycommand-feedback.md#rb-api-wholebodycommand-feedback) |  |  |
| component_based_command_feedback | [ComponentBasedCommand.Feedback](../component_based_command/componentbasedcommand-feedback.md#rb-api-componentbasedcommand-feedback) |  |  |
| jog_command_feedback | [JogCommand.Feedback](../basic_command/jogcommand-feedback.md#rb-api-jogcommand-feedback) |  |  |
| status | [RobotCommand.Feedback.Status](robotcommand-feedback-status.md#rb-api-robotcommand-feedback-status) |  |  |
| finish_code | [RobotCommand.Feedback.FinishCode](robotcommand-feedback-finishcode.md#rb-api-robotcommand-feedback-finishcode) |  |  |
