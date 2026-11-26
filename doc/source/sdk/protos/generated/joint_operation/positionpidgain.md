(rb-api-positionpidgain)=
# PositionPIDGain

- Source proto: [`rb/api/joint_operation.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/joint_operation.proto) (rby1-sdk v0.10.1)

Position PID gains of one joint motor driver.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| timestamp | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| p_gain | [uint32](../scalar-value-types.md) |  |  |
| i_gain | [uint32](../scalar-value-types.md) |  |  |
| d_gain | [uint32](../scalar-value-types.md) |  |  |
