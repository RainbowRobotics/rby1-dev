(rb-api-setloglevelrequest)=
# SetLogLevelRequest

- Source proto: [`rb/api/log.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/log.proto) (rby1-sdk v0.10.1)

Request of the `SetLogLevel` RPC of [LogService](../log_service/logservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| level | [Log.Level](log-level.md) |  |  |
