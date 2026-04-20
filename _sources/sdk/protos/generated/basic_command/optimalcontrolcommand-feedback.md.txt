(rb-api-optimalcontrolcommand-feedback)=
# OptimalControlCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for OptimalControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| total_cost | [double](../scalar-value-types.md) |  |  |
| cartesian_costs | [double](../scalar-value-types.md) | repeated |  |
| center_of_mass_cost | [double](../scalar-value-types.md) |  |  |
| joint_position_costs | [double](../scalar-value-types.md) | repeated |  |
