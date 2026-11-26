(rb-api-gripperinitializationrequest)=
# GripperInitializationRequest

- Source proto: [`rb/api/gripper_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/gripper_command.proto) (rby1-sdk v0.10.1)

Initialize a gripper by name and prepare it for motion.

Request of the `GripperInitialization` RPC of [GripperCommandService](../gripper_command_service/grippercommandservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  |  |
