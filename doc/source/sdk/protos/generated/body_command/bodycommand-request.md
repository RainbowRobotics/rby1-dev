(rb-api-bodycommand-request)=
# BodyCommand.Request

- Source proto: [`rb/api/body_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/body_command.proto) (rby1-sdk v0.10.1)

Request part of [BodyCommand](bodycommand.md).

Only one field of the `command` oneof can be set at a time: `joint_position_command`, `optimal_control_command`, `gravity_compensation_command`, `cartesian_command`, `body_component_based_command`, `joint_impedance_control_command`, `cartesian_impedance_control_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md) | oneof command |  |
| optimal_control_command | [OptimalControlCommand.Request](../basic_command/optimalcontrolcommand-request.md) | oneof command |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md) | oneof command |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md) | oneof command |  |
| body_component_based_command | [BodyComponentBasedCommand.Request](../body_component_based_command/bodycomponentbasedcommand-request.md) | oneof command |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md) | oneof command |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md) | oneof command |  |
