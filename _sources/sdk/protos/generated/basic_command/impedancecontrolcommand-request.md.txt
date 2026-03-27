# ImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for ImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| ref_link_name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| link_name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| T | [SE3Pose](../geometry/se3pose.md#rb-api-se3pose) |  |  |
| translation_weight | [Vec3](../geometry/vec3.md#rb-api-vec3) |  | Translation part of stiffness |
| rotation_weight | [Vec3](../geometry/vec3.md#rb-api-vec3) |  | Rotation part of stiffness |
| damping_ratio | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1 |
