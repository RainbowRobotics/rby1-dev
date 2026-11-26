(rb-api-wholebodycommand-feedback)=
# WholeBodyCommand.Feedback

- Source proto: [`rb/api/whole_body_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/whole_body_command.proto) (rby1-sdk v0.10.1)

Feedback part of [WholeBodyCommand](wholebodycommand.md).

Only one field of the `feedback` oneof can be set at a time: `stop_command_feedback`, `real_time_control_command_feedback`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| stop_command_feedback | [StopCommand.Feedback](../basic_command/stopcommand-feedback.md) | oneof feedback |  |
| real_time_control_command_feedback | [RealTimeControlCommand.Feedback](../basic_command/realtimecontrolcommand-feedback.md) | oneof feedback |  |
