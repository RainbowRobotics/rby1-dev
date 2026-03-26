# RobotCommandService

- Source proto: `rb/api/robot_command_service.proto`

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| RobotCommand | [RobotCommandRequest](./robotcommandrequest.md#rb-api-robotcommandrequest) | [RobotCommandResponse](./robotcommandresponse.md#rb-api-robotcommandresponse) | In case of sending and receiving a single command |
| RobotCommandStream | [RobotCommandRequest](./robotcommandrequest.md#rb-api-robotcommandrequest) stream | [RobotCommandResponse](./robotcommandresponse.md#rb-api-robotcommandresponse) stream | In case of sending and receiving commands continuously |
