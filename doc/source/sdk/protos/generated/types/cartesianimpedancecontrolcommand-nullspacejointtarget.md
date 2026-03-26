# CartesianImpedanceControlCommand.NullspaceJointTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_position | [double](./scalar-value-types.md#scalar-value-types) | repeated | Length: DOF |
| weight | [double](./scalar-value-types.md#scalar-value-types) | repeated | Length: DOF, [0, inf), default = 1 |
| k_p | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 0.2 |
| k_d | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 0.2 |
| cost_weight | [google.protobuf.DoubleValue](#google-protobuf-DoubleValue) |  | default = 1e-3 |
