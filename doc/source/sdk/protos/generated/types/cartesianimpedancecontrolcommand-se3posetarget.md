# CartesianImpedanceControlCommand.SE3PoseTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| T | [SE3Pose](./se3pose.md#rb-api-se3pose) |  |  |
| linear_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s) |
| angular_velocity_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s) |
| linear_acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (m/s^2) |
| angular_acceleration_limit | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | (rad/s^2) |
