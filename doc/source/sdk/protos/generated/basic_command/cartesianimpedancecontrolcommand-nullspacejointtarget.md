(rb-api-cartesianimpedancecontrolcommand-nullspacejointtarget)=
# CartesianImpedanceControlCommand.NullspaceJointTarget

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| target_position | [double](../scalar-value-types.md) | repeated | Length: DOF |
| weight | [double](../scalar-value-types.md) | repeated | Length: DOF, [0, inf), default = 1 |
| k_p | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 0.2 |
| k_d | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 0.2 |
| cost_weight | [google.protobuf.DoubleValue](https://protobuf.dev/reference/protobuf/google.protobuf/#doublevalue) |  | default = 1e-3 |
