# ConnectWifiRequest

- Source proto: `rb/api/system.proto`

Request to connect wifi.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md#rb-api-requestheader) |  |  |
| ssid | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| password | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| use_dhcp | [bool](../scalar-value-types.md#scalar-value-types) |  |  |
| ip_address | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| gateway | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| dns | [string](../scalar-value-types.md#scalar-value-types) | repeated |  |
