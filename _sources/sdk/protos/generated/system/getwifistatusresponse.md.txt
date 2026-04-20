(rb-api-getwifistatusresponse)=
# GetWifiStatusResponse

- Source proto: `rb/api/system.proto`

Response for get wifi status.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| ssid | [string](../scalar-value-types.md) |  |  |
| ip_address | [string](../scalar-value-types.md) |  |  |
| gateway | [string](../scalar-value-types.md) |  |  |
| dns | [string](../scalar-value-types.md) | repeated |  |
| connected | [bool](../scalar-value-types.md) |  |  |
