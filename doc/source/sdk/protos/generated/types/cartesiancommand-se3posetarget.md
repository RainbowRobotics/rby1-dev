# CartesianCommand.SE3PoseTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| T | [SE3Pose](./se3pose.md#rb-api-se3pose) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) |
| acceleration_limit_scaling | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default.linear_acceleration_limit * acceleration_limit_scaling default.angular_acceleration_limit * acceleration_limit_scaling

`(0, 1]` |
