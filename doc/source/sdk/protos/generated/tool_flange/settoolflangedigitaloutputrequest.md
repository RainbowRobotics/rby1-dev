(rb-api-settoolflangedigitaloutputrequest)=
# SetToolFlangeDigitalOutputRequest

- Source proto: [`rb/api/tool_flange.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/tool_flange.proto) (rby1-sdk v0.10.1)

Request of the `SetDigitalOutput` RPC of [ToolFlangeService](../tool_flange_service/toolflangeservice.md).

Only one field of the `command` oneof can be set at a time: `single`, `dual`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| name | [string](../scalar-value-types.md) |  | tool flange name; &#39;left&#39; or &#39;right&#39; |
| single | [SetToolFlangeDigitalOutputRequest.SingleChannel](settoolflangedigitaloutputrequest-singlechannel.md) | oneof command |  |
| dual | [SetToolFlangeDigitalOutputRequest.DualChannel](settoolflangedigitaloutputrequest-dualchannel.md) | oneof command |  |
