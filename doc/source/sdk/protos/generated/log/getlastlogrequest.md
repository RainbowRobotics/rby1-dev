(rb-api-getlastlogrequest)=
# GetLastLogRequest

- Source proto: [`rb/api/log.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/log.proto) (rby1-sdk v0.10.1)

Request of the `GetLastLog` RPC of [LogService](../log_service/logservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| log_count | [int32](../scalar-value-types.md) |  |  |
