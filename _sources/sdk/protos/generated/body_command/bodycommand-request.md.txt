# BodyCommand.Request

- Source proto: `rb/api/body_command.proto`

Request payload for BodyCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md#rb-api-jointpositioncommand-request) |  |  |
| optimal_control_command | [OptimalControlCommand.Request](../basic_command/optimalcontrolcommand-request.md#rb-api-optimalcontrolcommand-request) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md#rb-api-gravitycompensationcommand-request) |  |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md#rb-api-cartesiancommand-request) |  |  |
| body_component_based_command | [BodyComponentBasedCommand.Request](../body_component_based_command/bodycomponentbasedcommand-request.md#rb-api-bodycomponentbasedcommand-request) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md#rb-api-jointimpedancecontrolcommand-request) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md#rb-api-cartesianimpedancecontrolcommand-request) |  |  |
