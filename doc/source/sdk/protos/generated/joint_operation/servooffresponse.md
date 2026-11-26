(rb-api-servooffresponse)=
# ServoOffResponse

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Response of the `ServoOff` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  | Response header |
| status | [ServoOffResponse.Status](servooffresponse-status.md) |  |  |
| message | [string](../scalar-value-types.md) |  |  |
