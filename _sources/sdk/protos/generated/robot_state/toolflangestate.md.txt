(rb-api-toolflangestate)=
# ToolFlangeState

- Source proto: `rb/api/robot_state.proto`

State snapshot for tool flange.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| gyro | [Vec3](../geometry/vec3.md) |  |  |
| acceleration | [Vec3](../geometry/vec3.md) |  |  |
| switch_A | [bool](../scalar-value-types.md) |  |  |
| output_voltage | [int32](../scalar-value-types.md) |  |  |
| digital_input_A | [bool](../scalar-value-types.md) |  |  |
| digital_input_B | [bool](../scalar-value-types.md) |  |  |
| digital_output_A | [bool](../scalar-value-types.md) |  |  |
| digital_output_B | [bool](../scalar-value-types.md) |  |  |
