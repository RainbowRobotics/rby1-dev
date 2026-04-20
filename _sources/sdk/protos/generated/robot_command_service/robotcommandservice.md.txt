(rb-api-robotcommandservice)=
# RobotCommandService

- Source proto: `rb/api/robot_command_service.proto`

gRPC service for robot command.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](../robot_command/robotcommandrequest.md) | [RobotCommandResponse](../robot_command/robotcommandresponse.md) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](../robot_command/robotcommandrequest.md) stream | [RobotCommandResponse](../robot_command/robotcommandresponse.md) stream | In case of sending and receiving commands continuously |
