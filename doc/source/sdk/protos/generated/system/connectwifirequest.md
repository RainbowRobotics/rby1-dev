(rb-api-connectwifirequest)=
# ConnectWifiRequest

- Source proto: [`rb/api/system.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/system.proto) (rby1-sdk v0.10.1)

Request of the `ConnectWifi` RPC of [SystemService](../system_service/systemservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| ssid | [string](../scalar-value-types.md) |  |  |
| password | [string](../scalar-value-types.md) |  |  |
| use_dhcp | [bool](../scalar-value-types.md) |  |  |
| ip_address | [string](../scalar-value-types.md) |  |  |
| gateway | [string](../scalar-value-types.md) |  |  |
| dns | [string](../scalar-value-types.md) | repeated |  |
