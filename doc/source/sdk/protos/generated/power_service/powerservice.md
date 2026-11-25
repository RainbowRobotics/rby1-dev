(rb-api-powerservice)=
# PowerService

- Source proto: `rb/api/power_service.proto`

gRPC service for power.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PowerCommand | [PowerCommandRequest](../power/powercommandrequest.md) | [PowerCommandResponse](../power/powercommandresponse.md) | Control power of the robot |
| JointCommand | [JointCommandRequest](../power/jointcommandrequest.md) | [JointCommandResponse](../power/jointcommandresponse.md) | Joint command |
| ToolFlangePowerCommand | [ToolFlangePowerCommandRequest](../power/toolflangepowercommandrequest.md) | [ToolFlangePowerCommandResponse](../power/toolflangepowercommandresponse.md) | Tool Flange |
