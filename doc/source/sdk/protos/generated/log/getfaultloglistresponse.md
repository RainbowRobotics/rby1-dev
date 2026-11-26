(rb-api-getfaultloglistresponse)=
# GetFaultLogListResponse

- Source proto: [`rb/api/log.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/log.proto) (rby1-sdk v0.10.1)

Response of the `GetFaultLogList` RPC of [LogService](../log_service/logservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| fault_log_list | [string](../scalar-value-types.md) | repeated |  |
