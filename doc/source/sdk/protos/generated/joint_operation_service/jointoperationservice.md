# JointOperationService

- Source proto: `rb/api/joint_operation_service.proto`

gRPC service for joint operation.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ServoOn | [ServoOnRequest](../joint_operation/servoonrequest.md#rb-api-servoonrequest) | [ServoOnResponse](../joint_operation/servoonresponse.md#rb-api-servoonresponse) |  |
| ServoOff | [ServoOffRequest](../joint_operation/servooffrequest.md#rb-api-servooffrequest) | [ServoOffResponse](../joint_operation/servooffresponse.md#rb-api-servooffresponse) |  |
| BrakeEngage | [BrakeEngageRequest](../joint_operation/brakeengagerequest.md#rb-api-brakeengagerequest) | [BrakeEngageResponse](../joint_operation/brakeengageresponse.md#rb-api-brakeengageresponse) |  |
| BrakeRelease | [BrakeReleaseRequest](../joint_operation/brakereleaserequest.md#rb-api-brakereleaserequest) | [BrakeReleaseResponse](../joint_operation/brakereleaseresponse.md#rb-api-brakereleaseresponse) |  |
| HomeOffsetReset | [HomeOffsetResetRequest](../joint_operation/homeoffsetresetrequest.md#rb-api-homeoffsetresetrequest) | [HomeOffsetResetResponse](../joint_operation/homeoffsetresetresponse.md#rb-api-homeoffsetresetresponse) |  |
| GetPositionPIDGain | [GetPositionPIDGainRequest](../joint_operation/getpositionpidgainrequest.md#rb-api-getpositionpidgainrequest) | [GetPositionPIDGainResponse](../joint_operation/getpositionpidgainresponse.md#rb-api-getpositionpidgainresponse) |  |
| SetPositionPIDGain | [SetPositionPIDGainRequest](../joint_operation/setpositionpidgainrequest.md#rb-api-setpositionpidgainrequest) | [SetPositionPIDGainResponse](../joint_operation/setpositionpidgainresponse.md#rb-api-setpositionpidgainresponse) |  |
| SetPresetPosition | [SetPresetPositionRequest](../joint_operation/setpresetpositionrequest.md#rb-api-setpresetpositionrequest) | [SetPresetPositionResponse](../joint_operation/setpresetpositionresponse.md#rb-api-setpresetpositionresponse) |  |
