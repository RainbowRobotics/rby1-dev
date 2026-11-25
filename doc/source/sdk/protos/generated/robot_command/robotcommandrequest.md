(rb-api-robotcommandrequest)=
# RobotCommandRequest

- Source proto: `rb/api/robot_command.proto`

RPC request wrapper for sending a robot command with priority.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| robot_command | [RobotCommand.Request](robotcommand-request.md) |  |  |
| priority | [int32](../scalar-value-types.md) |  |  |
