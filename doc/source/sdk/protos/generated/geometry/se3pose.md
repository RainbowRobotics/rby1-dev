(rb-api-se3pose)=
# SE3Pose

- Source proto: [`rb/api/geometry.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/geometry.proto) (rby1-sdk v0.10.1)

Pose representation in SE3 space.

Only one field of the `rotation` oneof can be set at a time: `quaternion`, `euler`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| position | [Vec3](vec3.md) |  | (m) |
| quaternion | [Quaternion](quaternion.md) | oneof rotation |  |
| euler | [EulerAngleZYX](euleranglezyx.md) | oneof rotation |  |
