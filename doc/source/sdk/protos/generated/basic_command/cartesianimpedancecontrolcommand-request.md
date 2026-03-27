# CartesianImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for CartesianImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  | default = 0 |
| targets | [CartesianImpedanceControlCommand.SE3PoseTarget](cartesianimpedancecontrolcommand-se3posetarget.md#rb-api-cartesianimpedancecontrolcommand-se3posetarget) | repeated |  |
| joint_position_targets | [CartesianImpedanceControlCommand.JointPositionTarget](cartesianimpedancecontrolcommand-jointpositiontarget.md#rb-api-cartesianimpedancecontrolcommand-jointpositiontarget) | repeated |  |
| stop_position_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
| stop_orientation_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
| stop_joint_position_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
| joint_stiffness | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| joint_damping_ratio | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1 |
| joint_torque_limit | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| joint_limits | [CartesianImpedanceControlCommand.JointLimit](cartesianimpedancecontrolcommand-jointlimit.md#rb-api-cartesianimpedancecontrolcommand-jointlimit) | repeated |  |
| reset_reference | [google.protobuf.BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#boolvalue) |  | default = false |
| nullspace_joint_target | [CartesianImpedanceControlCommand.NullspaceJointTarget](cartesianimpedancecontrolcommand-nullspacejointtarget.md#rb-api-cartesianimpedancecontrolcommand-nullspacejointtarget) |  |  |
