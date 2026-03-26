# ImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](./commandheader-request.md#rb-api-commandheader-request) |  |  |
| ref_link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| link_name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| T | [SE3Pose](./se3pose.md#rb-api-se3pose) |  |  |
| translation_weight | [Vec3](./vec3.md#rb-api-vec3) |  | Translation part of stiffness |
| rotation_weight | [Vec3](./vec3.md#rb-api-vec3) |  | Rotation part of stiffness |
| damping_ratio | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1 |
