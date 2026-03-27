# JointPositionCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for JointPositionCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| time_based_progress | [double](../scalar-value-types.md#scalar-value-types) |  | [0, 1] |
| position_based_progress | [double](../scalar-value-types.md#scalar-value-types) |  | (-inf, 1] |
