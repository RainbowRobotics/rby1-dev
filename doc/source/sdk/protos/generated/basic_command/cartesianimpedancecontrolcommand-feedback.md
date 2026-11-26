(rb-api-cartesianimpedancecontrolcommand-feedback)=
# CartesianImpedanceControlCommand.Feedback

- Source proto: [`rb/api/basic_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/basic_command.proto) (rby1-sdk v0.10.1)

Feedback part of [CartesianImpedanceControlCommand](cartesianimpedancecontrolcommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| set_position | [double](../scalar-value-types.md) | repeated |  |
| remain_time | [double](../scalar-value-types.md) |  |  |
| manipulability | [double](../scalar-value-types.md) |  |  |
