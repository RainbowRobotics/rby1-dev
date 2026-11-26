(rb-api-getpositionpidgainrequest)=
# GetPositionPIDGainRequest

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Request of the `GetPositionPIDGain` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

Only one field of the `command` oneof can be set at a time: `dev_name`, `target_component`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| dev_name | [string](../scalar-value-types.md) | oneof command |  |
| target_component | [GetPositionPIDGainRequest.TargetComponent](getpositionpidgainrequest-targetcomponent.md) | oneof command |  |
