(rb-api-responseheader)=
# ResponseHeader

- Source proto: [`rb/api/header.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/header.proto) (rby1-sdk v0.10.1)

Standard response header


| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](requestheader.md) |  | Echo |
| request_received_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  | Robot clock |
| response_timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  | Robot clock |
| error | [CommonError](commonerror.md) |  | If set, there is error |
