(rb-api-controlmanagerservice)=
# ControlManagerService

- Source proto: [`rb/api/control_manager_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/control_manager_service.proto) (rby1-sdk v0.10.1)

Enables and disables the Control Manager, resets faults, cancels the running control, sets the time scale and waits until the robot is ready for commands.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ControlManagerCommand | [ControlManagerCommandRequest](../control_manager/controlmanagercommandrequest.md) | [ControlManagerCommandResponse](../control_manager/controlmanagercommandresponse.md) |  |
| CancelControl | [CancelControlRequest](../control_manager/cancelcontrolrequest.md) | [CancelControlResponse](../control_manager/cancelcontrolresponse.md) |  |
| GetTimeScale | [GetTimeScaleRequest](../control_manager/gettimescalerequest.md) | [GetTimeScaleResponse](../control_manager/gettimescaleresponse.md) |  |
| SetTimeScale | [SetTimeScaleRequest](../control_manager/settimescalerequest.md) | [SetTimeScaleResponse](../control_manager/settimescaleresponse.md) |  |
| WaitForControlReady | [WaitForControlReadyRequest](../control_manager/waitforcontrolreadyrequest.md) | [WaitForControlReadyResponse](../control_manager/waitforcontrolreadyresponse.md) |  |
