# CartesianCommand.Feedback

- Source proto: `rb/api/basic_command.proto`

Feedback payload for CartesianCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md#rb-api-commandheader-feedback) |  |  |
| se3_pose_tracking_errors | [CartesianCommand.TrackingError](cartesiancommand-trackingerror.md#rb-api-cartesiancommand-trackingerror) | repeated |  |
| joint_position_tracking_errors | [double](../scalar-value-types.md#scalar-value-types) | repeated |  |
| remain_time | [double](../scalar-value-types.md#scalar-value-types) |  |  |
| manipulability | [double](../scalar-value-types.md#scalar-value-types) |  |  |
