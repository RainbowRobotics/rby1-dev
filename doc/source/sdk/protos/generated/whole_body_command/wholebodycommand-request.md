(rb-api-wholebodycommand-request)=
# WholeBodyCommand.Request

- Source proto: [`rb/api/whole_body_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/whole_body_command.proto) (rby1-sdk v0.10.1)

Request part of [WholeBodyCommand](wholebodycommand.md).

Only one field of the `command` oneof can be set at a time: `stop_command`, `real_time_control_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| stop_command | [StopCommand.Request](../basic_command/stopcommand-request.md) | oneof command |  |
| real_time_control_command | [RealTimeControlCommand.Request](../basic_command/realtimecontrolcommand-request.md) | oneof command |  |
