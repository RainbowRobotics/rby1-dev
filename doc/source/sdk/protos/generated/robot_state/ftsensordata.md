(rb-api-ftsensordata)=
# FTSensorData

- Source proto: [`rb/api/robot_state.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_state.proto) (rby1-sdk v0.10.1)

Force and torque measured by a force/torque sensor, and the time since its last update.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| force | [Vec3](../geometry/vec3.md) |  |  |
| torque | [Vec3](../geometry/vec3.md) |  |  |
