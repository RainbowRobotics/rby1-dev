# BodyCommand.Feedback

- Source proto: `rb/api/body_command.proto`

Feedback payload for BodyCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](../basic_command/jointpositioncommand-feedback.md#rb-api-jointpositioncommand-feedback) |  |  |
| optimal_control_command_feedback | [OptimalControlCommand.Feedback](../basic_command/optimalcontrolcommand-feedback.md#rb-api-optimalcontrolcommand-feedback) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](../basic_command/gravitycompensationcommand-feedback.md#rb-api-gravitycompensationcommand-feedback) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](../basic_command/cartesiancommand-feedback.md#rb-api-cartesiancommand-feedback) |  |  |
| body_component_based_command_feedback | [BodyComponentBasedCommand.Feedback](../body_component_based_command/bodycomponentbasedcommand-feedback.md#rb-api-bodycomponentbasedcommand-feedback) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](../basic_command/jointimpedancecontrolcommand-feedback.md#rb-api-jointimpedancecontrolcommand-feedback) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](../basic_command/cartesianimpedancecontrolcommand-feedback.md#rb-api-cartesianimpedancecontrolcommand-feedback) |  |  |
