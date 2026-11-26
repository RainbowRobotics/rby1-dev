(rb-api-powerservice)=
# PowerService

- Source proto: [`rb/api/power_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/power_service.proto) (rby1-sdk v0.10.1)

Turns power outputs on and off, sends joint commands (servo on, brakes, home offset) and sets the tool flange power.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PowerCommand | [PowerCommandRequest](../power/powercommandrequest.md) | [PowerCommandResponse](../power/powercommandresponse.md) | Turns the named power outputs on or off. |
| JointCommand | [JointCommandRequest](../power/jointcommandrequest.md) | [JointCommandResponse](../power/jointcommandresponse.md) | Runs a joint command (servo on, brake engage, brake release or home offset reset) on the named joints. Brake release and home offset reset have the same risks as in JointOperationService. |
| ToolFlangePowerCommand | [ToolFlangePowerCommandRequest](../power/toolflangepowercommandrequest.md) | [ToolFlangePowerCommandResponse](../power/toolflangepowercommandresponse.md) | Sets the tool flange power: off, 12 V or 24 V. |
