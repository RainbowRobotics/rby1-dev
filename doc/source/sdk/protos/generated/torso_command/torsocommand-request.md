(rb-api-torsocommand-request)=
# TorsoCommand.Request

- Source proto: [`rb/api/torso_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/torso_command.proto) (rby1-sdk v0.10.1)

Request part of [TorsoCommand](torsocommand.md).

Only one field of the `command` oneof can be set at a time: `joint_position_command`, `gravity_compensation_command`, `cartesian_command`, `impedance_control_command`, `optimal_control_command`, `joint_impedance_control_command`, `cartesian_impedance_control_command`, `joint_group_position_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_position_command | [JointPositionCommand.Request](../basic_command/jointpositioncommand-request.md) | oneof command |  |
| gravity_compensation_command | [GravityCompensationCommand.Request](../basic_command/gravitycompensationcommand-request.md) | oneof command |  |
| cartesian_command | [CartesianCommand.Request](../basic_command/cartesiancommand-request.md) | oneof command |  |
| impedance_control_command | [ImpedanceControlCommand.Request](../basic_command/impedancecontrolcommand-request.md) | oneof command |  |
| optimal_control_command | [OptimalControlCommand.Request](../basic_command/optimalcontrolcommand-request.md) | oneof command |  |
| joint_impedance_control_command | [JointImpedanceControlCommand.Request](../basic_command/jointimpedancecontrolcommand-request.md) | oneof command |  |
| cartesian_impedance_control_command | [CartesianImpedanceControlCommand.Request](../basic_command/cartesianimpedancecontrolcommand-request.md) | oneof command |  |
| joint_group_position_command | [JointGroupPositionCommand.Request](../basic_command/jointgrouppositioncommand-request.md) | oneof command |  |
