(rb-api-jointoperationservice)=
# JointOperationService

- Source proto: `rb/api/joint_operation_service.proto`

gRPC service for joint operation.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| ServoOn | [ServoOnRequest](../joint_operation/servoonrequest.md) | [ServoOnResponse](../joint_operation/servoonresponse.md) |  |
| ServoOff | [ServoOffRequest](../joint_operation/servooffrequest.md) | [ServoOffResponse](../joint_operation/servooffresponse.md) |  |
| BrakeEngage | [BrakeEngageRequest](../joint_operation/brakeengagerequest.md) | [BrakeEngageResponse](../joint_operation/brakeengageresponse.md) |  |
| BrakeRelease | [BrakeReleaseRequest](../joint_operation/brakereleaserequest.md) | [BrakeReleaseResponse](../joint_operation/brakereleaseresponse.md) |  |
| HomeOffsetReset | [HomeOffsetResetRequest](../joint_operation/homeoffsetresetrequest.md) | [HomeOffsetResetResponse](../joint_operation/homeoffsetresetresponse.md) |  |
| GetPositionPIDGain | [GetPositionPIDGainRequest](../joint_operation/getpositionpidgainrequest.md) | [GetPositionPIDGainResponse](../joint_operation/getpositionpidgainresponse.md) |  |
| SetPositionPIDGain | [SetPositionPIDGainRequest](../joint_operation/setpositionpidgainrequest.md) | [SetPositionPIDGainResponse](../joint_operation/setpositionpidgainresponse.md) |  |
| SetPresetPosition | [SetPresetPositionRequest](../joint_operation/setpresetpositionrequest.md) | [SetPresetPositionResponse](../joint_operation/setpresetpositionresponse.md) |  |
