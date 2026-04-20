(rb-api-cartesiancommand-request)=
# CartesianCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for CartesianCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| minimum_time | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| targets | [CartesianCommand.SE3PoseTarget](cartesiancommand-se3posetarget.md) | repeated |  |
| joint_position_targets | [CartesianCommand.JointPositionTarget](cartesiancommand-jointpositiontarget.md) | repeated |  |
| stop_position_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
| stop_orientation_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
| stop_joint_position_tracking_error | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  |  |
