(rb-api-jointpositioncommand-feedback)=
# JointPositionCommand.Feedback

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Feedback part of [JointPositionCommand](jointpositioncommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| time_based_progress | [double](../scalar-value-types.md) |  | [0, 1] |
| position_based_progress | [double](../scalar-value-types.md) |  | (-inf, 1] |
