(rb-api-robotcommand-request)=
# RobotCommand.Request

- Source proto: [`rb/api/robot_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/robot_command.proto) (rby1-sdk v0.10.1)

Request part of [RobotCommand](robotcommand.md).

Only one field of the `command` oneof can be set at a time: `whole_body_command`, `component_based_command`, `jog_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| whole_body_command | [WholeBodyCommand.Request](../whole_body_command/wholebodycommand-request.md) | oneof command |  |
| component_based_command | [ComponentBasedCommand.Request](../component_based_command/componentbasedcommand-request.md) | oneof command |  |
| jog_command | [JogCommand.Request](../basic_command/jogcommand-request.md) | oneof command |  |
