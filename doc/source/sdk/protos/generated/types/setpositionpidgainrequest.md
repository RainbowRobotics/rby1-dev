# SetPositionPIDGainRequest

- Source proto: `rb/api/joint_operation.proto`

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](./requestheader.md#rb-api-requestheader) |  | Request header |
| name | [string](./scalar-value-types.md#scalar-value-types) |  |  |
| p_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| i_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
| d_gain | [google.protobuf.UInt32Value](#google-protobuf-UInt32Value) |  |  |
