(rb-api-jointinfo)=
# JointInfo

- Source proto: [`rb/api/robot_info.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_info.proto) (rby1-sdk v0.10.1)

Static information about one joint: name, brake, motor product and firmware version.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| name | [string](../scalar-value-types.md) |  | Joint Motor Name |
| has_brake | [bool](../scalar-value-types.md) |  | Whether the joint has a brake |
| product_name | [string](../scalar-value-types.md) |  | RB or Dynamixel |
| firmware_version | [string](../scalar-value-types.md) |  | Firmware Version Name |
