(rb-api-collision)=
# Collision

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

One pair of links that are close to each other or in collision, with the closest points and their distance.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| link1 | [string](../scalar-value-types.md) |  |  |
| link2 | [string](../scalar-value-types.md) |  |  |
| position1 | [Vec3](../geometry/vec3.md) |  |  |
| position2 | [Vec3](../geometry/vec3.md) |  |  |
| distance | [double](../scalar-value-types.md) |  |  |
