(rb-api-settoolflangedigitaloutputrequest)=
# SetToolFlangeDigitalOutputRequest

- Source proto: `rb/api/tool_flange.proto`

Request to set tool flange digital output.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| name | [string](../scalar-value-types.md) |  | tool flange name; &#39;left&#39; or &#39;right&#39; |
| single | [SetToolFlangeDigitalOutputRequest.SingleChannel](settoolflangedigitaloutputrequest-singlechannel.md) |  |  |
| dual | [SetToolFlangeDigitalOutputRequest.DualChannel](settoolflangedigitaloutputrequest-dualchannel.md) |  |  |
