# JointGroupPositionCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](./commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| joint_indices | [int32](./scalar-value-types.md#scalar-value-types) | repeated |  |
| time_based_progress | [double](./scalar-value-types.md#scalar-value-types) |  | [0, 1] |
| position_based_progress | [double](./scalar-value-types.md#scalar-value-types) |  | (-inf, 1] |
