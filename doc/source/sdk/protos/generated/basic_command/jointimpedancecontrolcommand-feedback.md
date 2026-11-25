(rb-api-jointimpedancecontrolcommand-feedback)=
# JointImpedanceControlCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for JointImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| set_position | [double](../scalar-value-types.md) | repeated |  |
| error | [double](../scalar-value-types.md) | repeated |  |
