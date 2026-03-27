# RobotCommand.Request

- Source proto: `rb/api/robot_command.proto`

Request payload for RobotCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| whole_body_command | [WholeBodyCommand.Request](../whole_body_command/wholebodycommand-request.md#rb-api-wholebodycommand-request) |  |  |
| component_based_command | [ComponentBasedCommand.Request](../component_based_command/componentbasedcommand-request.md#rb-api-componentbasedcommand-request) |  |  |
| jog_command | [JogCommand.Request](../basic_command/jogcommand-request.md#rb-api-jogcommand-request) |  |  |
