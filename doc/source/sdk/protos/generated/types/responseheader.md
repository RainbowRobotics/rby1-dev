# ResponseHeader

- Source proto: `rb/api/header.proto`

Standard response header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](./requestheader.md#rb-api-requestheader) |  | Echo |
| request_received_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| response_timestamp | [google.protobuf.Timestamp](#google-protobuf-Timestamp) |  | Robot clock |
| error | [CommonError](./commonerror.md#rb-api-commonerror) |  | If set, there is error |
