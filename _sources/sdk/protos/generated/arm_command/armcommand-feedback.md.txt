(rb-api-armcommand-feedback)=
# ArmCommand.Feedback

- Source proto: `rb/api/arm_command.proto`

Feedback payload for ArmCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](../basic_command/jointpositioncommand-feedback.md) |  |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](../basic_command/gravitycompensationcommand-feedback.md) |  |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](../basic_command/cartesiancommand-feedback.md) |  |  |
| impedance_control_command_feedback | [ImpedanceControlCommand.Feedback](../basic_command/impedancecontrolcommand-feedback.md) |  |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](../basic_command/jointimpedancecontrolcommand-feedback.md) |  |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](../basic_command/cartesianimpedancecontrolcommand-feedback.md) |  |  |
