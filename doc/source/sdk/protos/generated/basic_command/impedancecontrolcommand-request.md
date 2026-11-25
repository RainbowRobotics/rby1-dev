(rb-api-impedancecontrolcommand-request)=
# ImpedanceControlCommand.Request

- Source proto: `rb/api/basic_command.proto`

Request payload for ImpedanceControlCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| ref_link_name | [string](../scalar-value-types.md) |  |  |
| link_name | [string](../scalar-value-types.md) |  |  |
| T | [SE3Pose](../geometry/se3pose.md) |  |  |
| translation_weight | [Vec3](../geometry/vec3.md) |  | Translation part of stiffness |
| rotation_weight | [Vec3](../geometry/vec3.md) |  | Rotation part of stiffness |
| damping_ratio | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1 |
