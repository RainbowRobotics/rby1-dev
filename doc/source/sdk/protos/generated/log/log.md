(rb-api-log)=
# Log

- Source proto: [`rb/api/log.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/log.proto) (rby1-sdk v0.10.1)

One log entry of the robot program, with its level and time stamps.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| robot_system_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| level | [Log.Level](log-level.md) |  |  |
| message | [string](../scalar-value-types.md) |  |  |
