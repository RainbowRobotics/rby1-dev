(rb-api-homeoffsetresetrequest)=
# HomeOffsetResetRequest

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Request of the `HomeOffsetReset` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

```{danger}
This sets the current position as the zero of the joint and overwrites the stored home offset. Every later position reading and command uses the new zero, so a wrong zero makes the robot move to wrong poses and can drive the joint past its real mechanical range. Use it only when a maintenance procedure tells you to.
```

See also: [Maintenance](../../../../maintenance/index.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Joint name, for example `right_arm_2`. Regex patterns are supported. |
