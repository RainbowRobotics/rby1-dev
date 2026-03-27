# GetWifiStatusResponse

- Source proto: `rb/api/system.proto`

Response for get wifi status.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md#rb-api-responseheader) |  |  |
| ssid | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| ip_address | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| gateway | [string](../scalar-value-types.md#scalar-value-types) |  |  |
| dns | [string](../scalar-value-types.md#scalar-value-types) | repeated |  |
| connected | [bool](../scalar-value-types.md#scalar-value-types) |  |  |
