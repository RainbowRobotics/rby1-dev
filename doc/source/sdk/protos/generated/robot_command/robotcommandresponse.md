(rb-api-robotcommandresponse)=
# RobotCommandResponse

- Source proto: [`rb/api/robot_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_command.proto) (rby1-sdk v0.10.1)

RPC response wrapper for a robot command.

Response of the `RobotCommand` RPC of [RobotCommandService](../robot_command_service/robotcommandservice.md). Response of the `RobotCommandStream` RPC of [RobotCommandService](../robot_command_service/robotcommandservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| feedback | [RobotCommand.Feedback](robotcommand-feedback.md) |  |  |
