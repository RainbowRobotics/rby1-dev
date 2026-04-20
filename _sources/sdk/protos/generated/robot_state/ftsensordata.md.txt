(rb-api-ftsensordata)=
# FTSensorData

- Source proto: `rb/api/robot_state.proto`

Message type: ft sensor data.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| time_since_last_update | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
| force | [Vec3](../geometry/vec3.md) |  |  |
| torque | [Vec3](../geometry/vec3.md) |  |  |
