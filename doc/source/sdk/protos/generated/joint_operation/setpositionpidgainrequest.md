(rb-api-setpositionpidgainrequest)=
# SetPositionPIDGainRequest

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Request of the `SetPositionPIDGain` RPC of [JointOperationService](../joint_operation_service/jointoperationservice.md).

```{warning}
The gains change on the motor driver at once. Wrong gains can make a joint oscillate or move abruptly the next time it is controlled. The robot rejects this request unless the Control Manager is idle.
```

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Joint name, for example `right_arm_2`. Regex patterns are supported. |
| p_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  | New P gain. Leave unset to keep the current value. |
| i_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  | New I gain. Leave unset to keep the current value. |
| d_gain | [google.protobuf.UInt32Value](https://protobuf.dev/reference/protobuf/google.protobuf/#uint32value) |  | New D gain. Leave unset to keep the current value. |
