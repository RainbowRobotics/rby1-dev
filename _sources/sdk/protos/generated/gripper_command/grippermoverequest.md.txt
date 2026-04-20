(rb-api-grippermoverequest)=
# GripperMoveRequest

- Source proto: `rb/api/gripper_command.proto`

Move a gripper to a target position with velocity/force limits.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  |  |
| position | [int32](../scalar-value-types.md) |  |  |
| velocity | [int32](../scalar-value-types.md) |  |  |
| force | [int32](../scalar-value-types.md) |  |  |
