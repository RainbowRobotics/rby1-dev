# SetPositionPIDGainRequest

- Source proto: `rb/api/joint_operation.proto`

Request to set position pid gain.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md#rb-api-requestheader) |  | Request header |
| name | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| p_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  |  |
| i_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  |  |
| d_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  |  |
