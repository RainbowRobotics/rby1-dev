(rb-api-robotcommandrequest)=
# RobotCommandRequest

- Source proto: [`rb/api/robot_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_command.proto) (rby1-sdk v0.10.1)

RPC request wrapper for sending a robot command with priority.

Request of the `RobotCommand` RPC of [RobotCommandService](../robot_command_service/robotcommandservice.md). Request of the `RobotCommandStream` RPC of [RobotCommandService](../robot_command_service/robotcommandservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| robot_command | [RobotCommand.Request](robotcommand-request.md) |  |  |
| priority | [int32](../scalar-value-types.md) |  |  |
