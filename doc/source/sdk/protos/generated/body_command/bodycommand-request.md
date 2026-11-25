(rb-api-bodycommand-request)=
# BodyCommand.Request

- Source proto: `rb/api/body_command.proto`

Request payload for BodyCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md) |  |  |
| optimal_control_command | [OptimalControlCommand.Request](../basic_command/optimalcontrolcommand-request.md) |  |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md) |  |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md) |  |  |
| body_component_based_command | [BodyComponentBasedCommand.Request](../body_component_based_command/bodycomponentbasedcommand-request.md) |  |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md) |  |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md) |  |  |
