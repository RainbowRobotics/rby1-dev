(rb-api-cartesiancommand-feedback)=
# CartesianCommand.Feedback

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Feedback part of [CartesianCommand](cartesiancommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| se3_pose_tracking_errors | [CartesianCommand.TrackingError](cartesiancommand-trackingerror.md) | repeated |  |
| joint_position_tracking_errors | [double](../scalar-value-types.md) | repeated |  |
| remain_time | [double](../scalar-value-types.md) |  |  |
| manipulability | [double](../scalar-value-types.md) |  |  |
