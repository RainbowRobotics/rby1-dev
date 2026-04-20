(rb-api-cartesiancommand-se3posetarget)=
# CartesianCommand.SE3PoseTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](../scalar-value-types.md) |  |  |
| link_name | [string](../scalar-value-types.md) |  |  |
| T | [SE3Pose](../geometry/se3pose.md) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | (rad/s) |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default.linear_acceleration_limit * acceleration_limit_scaling default.angular_acceleration_limit * acceleration_limit_scaling

`(0, 1]` |
