(rb-api-armcommand-feedback)=
# ArmCommand.Feedback

- Source proto: [`rb/api/arm_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/arm_command.proto) (rby1-sdk v0.10.1)

Feedback part of [ArmCommand](armcommand.md).

Only one field of the `feedback` oneof can be set at a time: `joint_position_command_feedback`, `gravity_compensation_command_feedback`, `cartesian_command_feedback`, `impedance_control_command_feedback`, `joint_impedance_control_command_feedback`, `cartesian_impedance_control_command_feedback`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| joint_position_command_feedback | [JointPositionCommand.Feedback](../basic_command/jointpositioncommand-feedback.md) | oneof feedback |  |
| gravity_compensation_command_feedback | [GravityCompensationCommand.Feedback](../basic_command/gravitycompensationcommand-feedback.md) | oneof feedback |  |
| cartesian_command_feedback | [CartesianCommand.Feedback](../basic_command/cartesiancommand-feedback.md) | oneof feedback |  |
| impedance_control_command_feedback | [ImpedanceControlCommand.Feedback](../basic_command/impedancecontrolcommand-feedback.md) | oneof feedback |  |
| joint_impedance_control_command_feedback | [JointImpedanceControlCommand.Feedback](../basic_command/jointimpedancecontrolcommand-feedback.md) | oneof feedback |  |
| cartesian_impedance_control_command_feedback | [CartesianImpedanceControlCommand.Feedback](../basic_command/cartesianimpedancecontrolcommand-feedback.md) | oneof feedback |  |
