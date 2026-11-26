(rb-api-optimalcontrolcommand-feedback)=
# OptimalControlCommand.Feedback

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Feedback part of [OptimalControlCommand](optimalcontrolcommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| total_cost | [double](../scalar-value-types.md) |  |  |
| cartesian_costs | [double](../scalar-value-types.md) | repeated |  |
| center_of_mass_cost | [double](../scalar-value-types.md) |  |  |
| joint_position_costs | [double](../scalar-value-types.md) | repeated |  |
