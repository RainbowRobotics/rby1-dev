(rb-api-powercommandrequest)=
# PowerCommandRequest

- Source proto: [`rb/api/power.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/power.proto) (rby1-sdk v0.10.1)

Request of the `PowerCommand` RPC of [PowerService](../power_service/powerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Required. Regex for the power outputs: `5v`, `12v`, `24v` and `48v`. The whole name must match. Use `.*` for all outputs, as the SDK examples do. An empty name matches no output, so nothing changes, and the call still returns STATUS_SUCCESS. |
| command | [PowerCommandRequest.Command](powercommandrequest-command.md) |  |  |
