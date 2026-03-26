# CartesianImpedanceControlCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for CartesianImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| set_position | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| remain_time | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| manipulability | [double](../scalar-value-types.md#scalar-value-types) |  |  |
