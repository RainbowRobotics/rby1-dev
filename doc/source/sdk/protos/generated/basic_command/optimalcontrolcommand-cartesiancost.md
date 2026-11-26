(rb-api-optimalcontrolcommand-cartesiancost)=
# OptimalControlCommand.CartesianCost

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ref_link_name | [string](../scalar-value-types.md) |  |  |
| link_name | [string](../scalar-value-types.md) |  |  |
| T | [SE3Pose](../geometry/se3pose.md) |  |  |
| translation_weight | [double](../scalar-value-types.md) |  | default = 1 |
| rotation_weight | [double](../scalar-value-types.md) |  | default = 1 |
