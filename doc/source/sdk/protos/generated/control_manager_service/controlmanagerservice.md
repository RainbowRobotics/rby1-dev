# ControlManagerService

- Source proto: `rb/api/control_manager_service.proto`

gRPC service for control manager.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ControlManagerCommand | [ControlManagerCommandRequest](../control_manager/controlmanagercommandrequest.md#rb-api-controlmanagercommandrequest) | [ControlManagerCommandResponse](../control_manager/controlmanagercommandresponse.md#rb-api-controlmanagercommandresponse) |  |
| CancelControl | [CancelControlRequest](../control_manager/cancelcontrolrequest.md#rb-api-cancelcontrolrequest) | [CancelControlResponse](../control_manager/cancelcontrolresponse.md#rb-api-cancelcontrolresponse) |  |
| GetTimeScale | [GetTimeScaleRequest](../control_manager/gettimescalerequest.md#rb-api-gettimescalerequest) | [GetTimeScaleResponse](../control_manager/gettimescaleresponse.md#rb-api-gettimescaleresponse) |  |
| SetTimeScale | [SetTimeScaleRequest](../control_manager/settimescalerequest.md#rb-api-settimescalerequest) | [SetTimeScaleResponse](../control_manager/settimescaleresponse.md#rb-api-settimescaleresponse) |  |
| WaitForControlReady | [WaitForControlReadyRequest](../control_manager/waitforcontrolreadyrequest.md#rb-api-waitforcontrolreadyrequest) | [WaitForControlReadyResponse](../control_manager/waitforcontrolreadyresponse.md#rb-api-waitforcontrolreadyresponse) |  |
