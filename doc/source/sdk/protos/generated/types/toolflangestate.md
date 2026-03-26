# ToolFlangeState

- Source proto: `rb/api/robot_state.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](#google-protobuf-Duration) |  |  |
| gyro | [Vec3](./vec3.md#rb-api-vec3) |  |  |
| acceleration | [Vec3](./vec3.md#rb-api-vec3) |  |  |
| switch_A | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
| output_voltage | [int32](./scalar-value-types.md#scalar-value-types) |  |  |
| digital_input_A | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
| digital_input_B | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
| digital_output_A | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
| digital_output_B | [bool](./scalar-value-types.md#scalar-value-types) |  |  |
