(rb-api-torsocommand-feedback)=
# TorsoCommand.Feedback

- Source proto: `rb/api/torso_command.proto`

Feedback payload for TorsoCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](../basic_command/jointpositioncommand-feedback.md) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](../basic_command/gravitycompensationcommand-feedback.md) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](../basic_command/cartesiancommand-feedback.md) |  |  |
| impedance_control_command_feedback | [ImpedanceControlCommand.Feedback](../basic_command/impedancecontrolcommand-feedback.md) |  |  |
| optimal_control_command_feedback | [OptimalControlCommand.Feedback](../basic_command/optimalcontrolcommand-feedback.md) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](../basic_command/jointimpedancecontrolcommand-feedback.md) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](../basic_command/cartesianimpedancecontrolcommand-feedback.md) |  |  |
| joint_group_position_command_feedback | [JointGroupPositionCommand.Feedback](../basic_command/jointgrouppositioncommand-feedback.md) |  |  |
