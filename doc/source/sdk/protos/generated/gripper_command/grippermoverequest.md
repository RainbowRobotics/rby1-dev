(rb-api-grippermoverequest)=
# GripperMoveRequest

- Source proto: [`rb/api/gripper_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/gripper_command.proto) (rby1-sdk v0.10.1)

Move a gripper to a target position with velocity/force limits.

Request of the `GripperMove` RPC of [GripperCommandService](../gripper_command_service/grippercommandservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  |  |
| position | [int32](../scalar-value-types.md) |  |  |
| velocity | [int32](../scalar-value-types.md) |  |  |
| force | [int32](../scalar-value-types.md) |  |  |
