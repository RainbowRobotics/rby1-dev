(rb-api-setbatterylevelrequest)=
# SetBatteryLevelRequest

- Source proto: [`rb/api/system.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/system.proto) (rby1-sdk v0.10.1)

Request of the `SetBatteryLevel` RPC of [SystemService](../system_service/systemservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| level | [double](../scalar-value-types.md) |  | [0, 100] |
