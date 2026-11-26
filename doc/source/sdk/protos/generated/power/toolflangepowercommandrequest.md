(rb-api-toolflangepowercommandrequest)=
# ToolFlangePowerCommandRequest

- Source proto: [`rb/api/power.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/power.proto) (rby1-sdk v0.10.1)

Request of the `ToolFlangePowerCommand` RPC of [PowerService](../power_service/powerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Tool Flange name |
| command | [ToolFlangePowerCommandRequest.Command](toolflangepowercommandrequest-command.md) |  |  |
