(rb-api-jointcommandresponse)=
# JointCommandResponse

- Source proto: [`rb/api/power.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/power.proto) (rby1-sdk v0.10.1)

Response of the `JointCommand` RPC of [PowerService](../power_service/powerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  | Response header |
| status | [JointCommandResponse.Status](jointcommandresponse-status.md) |  |  |
| message | [string](../scalar-value-types.md) |  | Human-readable message for status |
