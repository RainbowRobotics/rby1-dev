(rb-api-robotcommand-request)=
# RobotCommand.Request

- Source proto: `rb/api/robot_command.proto`

Request payload for RobotCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| whole_body_command | [WholeBodyCommand.Request](../whole_body_command/wholebodycommand-request.md) |  |  |
| component_based_command | [ComponentBasedCommand.Request](../component_based_command/componentbasedcommand-request.md) |  |  |
| jog_command | [JogCommand.Request](../basic_command/jogcommand-request.md) |  |  |
