(rb-api-inertial)=
# Inertial

- Source proto: [`rb/api/geometry.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/geometry.proto) (rby1-sdk v0.10.1)

Mass, center of mass and inertia tensor of a link.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| mass | [double](../scalar-value-types.md) |  | Mass (kg) |
| center_of_mass | [Vec3](vec3.md) |  | Center of mass (m) |
| inertia | [Inertia](inertia.md) |  | Inertia tensor |
