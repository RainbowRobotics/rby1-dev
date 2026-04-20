(rb-api-cartesianimpedancecontrolcommand-se3posetarget)=
# CartesianImpedanceControlCommand.SE3PoseTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](../scalar-value-types.md) |  |  |
| link_name | [string](../scalar-value-types.md) |  |  |
| T | [SE3Pose](../geometry/se3pose.md) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (rad/s) |
| linear_acceleration_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (m/s^2) |
| angular_acceleration_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (rad/s^2) |
