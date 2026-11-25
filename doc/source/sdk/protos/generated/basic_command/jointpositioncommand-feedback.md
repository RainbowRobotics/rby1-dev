(rb-api-jointpositioncommand-feedback)=
# JointPositionCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for JointPositionCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| time_based_progress | [double](../scalar-value-types.md) |  | [0, 1] |
| position_based_progress | [double](../scalar-value-types.md) |  | (-inf, 1] |
