(rb-api-connectwifirequest)=
# ConnectWifiRequest

- Source proto: `rb/api/system.proto`

Request to connect wifi.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| ssid | [string](../scalar-value-types.md) |  |  |
| password | [string](../scalar-value-types.md) |  |  |
| use_dhcp | [bool](../scalar-value-types.md) |  |  |
| ip_address | [string](../scalar-value-types.md) |  |  |
| gateway | [string](../scalar-value-types.md) |  |  |
| dns | [string](../scalar-value-types.md) | repeated |  |
