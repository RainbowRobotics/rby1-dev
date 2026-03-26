# PowerService

- Source proto: `rb/api/power_service.proto`

gRPC service for power.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| PowerCommand | [PowerCommandRequest](../power/powercommandrequest.md#rb-api-powercommandrequest) | [PowerCommandResponse](../power/powercommandresponse.md#rb-api-powercommandresponse) | Control power of the robot |
| JointCommand | [JointCommandRequest](../power/jointcommandrequest.md#rb-api-jointcommandrequest) | [JointCommandResponse](../power/jointcommandresponse.md#rb-api-jointcommandresponse) | Joint command |
| ToolFlangePowerCommand | [ToolFlangePowerCommandRequest](../power/toolflangepowercommandrequest.md#rb-api-toolflangepowercommandrequest) | [ToolFlangePowerCommandResponse](../power/toolflangepowercommandresponse.md#rb-api-toolflangepowercommandresponse) | Tool Flange |
