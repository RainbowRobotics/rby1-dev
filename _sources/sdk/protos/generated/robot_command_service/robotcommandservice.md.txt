# RobotCommandService

- Source proto: `rb/api/robot_command_service.proto`

gRPC service for robot command.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](../robot_command/robotcommandrequest.md#rb-api-robotcommandrequest) | [RobotCommandResponse](../robot_command/robotcommandresponse.md#rb-api-robotcommandresponse) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](../robot_command/robotcommandrequest.md#rb-api-robotcommandrequest) stream | [RobotCommandResponse](../robot_command/robotcommandresponse.md#rb-api-robotcommandresponse) stream | In case of sending and receiving commands continuously |
