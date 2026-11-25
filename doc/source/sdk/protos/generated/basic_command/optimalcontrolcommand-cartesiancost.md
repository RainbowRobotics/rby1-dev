(rb-api-optimalcontrolcommand-cartesiancost)=
# OptimalControlCommand.CartesianCost

- Source proto: `rb/api/basic_command.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](../scalar-value-types.md) |  |  |
| link_name | [string](../scalar-value-types.md) |  |  |
| T | [SE3Pose](../geometry/se3pose.md) |  |  |
| translation_weight | [double](../scalar-value-types.md) |  | default = 1 |
| rotation_weight | [double](../scalar-value-types.md) |  | default = 1 |
