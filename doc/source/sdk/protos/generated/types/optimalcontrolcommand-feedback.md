# OptimalControlCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](./commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| total_cost | [double](./scalar-value-types.md#scalar-value-types) |  |  |
| cartesian_costs | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
| center_of_mass_cost | [double](./scalar-value-types.md#scalar-value-types) |  |  |
| joint_position_costs | [double](./scalar-value-types.md#scalar-value-types) | repeated |  |
