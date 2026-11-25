(rb-api-torsocommand-request)=
# TorsoCommand.Request

- Source proto: `rb/api/torso_command.proto`

Request payload for TorsoCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md) |  |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md) |  |  |
| impedance_control_command | [ImpedanceControlCommand.Request](../basic_command/impedancecontrolcommand-request.md) |  |  |
| optimal_control_command | [OptimalControlCommand.Request](../basic_command/optimalcontrolcommand-request.md) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md) |  |  |
| joint_group_position_command | [JointGroupPositionCommand.Request](../basic_command/jointgrouppositioncommand-request.md) |  |  |
