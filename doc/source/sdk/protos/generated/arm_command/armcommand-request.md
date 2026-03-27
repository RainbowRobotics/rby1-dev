# ArmCommand.Request

- Source proto: `rb/api/arm_command.proto`

Request payload for ArmCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md#rb-api-jointpositioncommand-request) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md#rb-api-gravitycompensationcommand-request) |  |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md#rb-api-cartesiancommand-request) |  |  |
| impedance_control_command | [ImpedanceControlCommand.Request](../basic_command/impedancecontrolcommand-request.md#rb-api-impedancecontrolcommand-request) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md#rb-api-jointimpedancecontrolcommand-request) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md#rb-api-cartesianimpedancecontrolcommand-request) |  |  |
