(rb-api-log)=
# Log

- Source proto: `rb/api/log.proto`

Message type: log.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| robot_system_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| level | [Log.Level](log-level.md) |  |  |
| message | [string](../scalar-value-types.md) |  |  |
