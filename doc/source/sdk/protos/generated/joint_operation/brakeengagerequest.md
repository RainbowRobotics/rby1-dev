(rb-api-brakeengagerequest)=
# BrakeEngageRequest

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Request of the `BrakeEngage` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Joint name, for example `right_arm_2`. Regex patterns are supported. |
