(rb-api-brakereleaserequest)=
# BrakeReleaseRequest

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Request of the `BrakeRelease` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

```{danger}
A joint whose servo is off is held only by its brake. When you release the brake, the joint can fall under gravity. Support the arm or torso and keep people clear before you release a brake.
```

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Joint name, for example `right_arm_2`. Regex patterns are supported. |
