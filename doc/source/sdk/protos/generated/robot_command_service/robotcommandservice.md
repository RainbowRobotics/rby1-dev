(rb-api-robotcommandservice)=
# RobotCommandService

- Source proto: [`rb/api/robot_command_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_command_service.proto) (rby1-sdk v0.10.1)

Sends robot commands: one command with RobotCommand, or a continuous stream of commands with RobotCommandStream.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](../robot_command/robotcommandrequest.md) | [RobotCommandResponse](../robot_command/robotcommandresponse.md) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](../robot_command/robotcommandrequest.md) stream | [RobotCommandResponse](../robot_command/robotcommandresponse.md) stream | In case of sending and receiving commands continuously |
