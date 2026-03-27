# OptimalControlCommand.CartesianCost

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| link_name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| T | [SE3Pose](../geometry/se3pose.md#rb-api-se3pose) |  |  |
| translation_weight | [double](../scalar-value-types.md#scalar-value-types) |  | default = 1 |
| rotation_weight | [double](../scalar-value-types.md#scalar-value-types) |  | default = 1 |
