(rb-api-responseheader)=
# ResponseHeader

- Source proto: `rb/api/header.proto`

Common header for response requests and responses.

Standard response header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](requestheader.md) |  | Echo |
| request_received_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  | Robot clock |
| response_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  | Robot clock |
| error | [CommonError](commonerror.md) |  | If set, there is error |
