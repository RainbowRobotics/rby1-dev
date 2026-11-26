(rb-api-mobilitycommand-feedback)=
# MobilityCommand.Feedback

- Source proto: [`rb/api/mobility_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/mobility_command.proto) (rby1-sdk v0.10.1)

Feedback part of [MobilityCommand](mobilitycommand.md).

Only one field of the `feedback` oneof can be set at a time: `joint_velocity_command_feedback`, `se2_velocity_command_feedback`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header_feedback | [CommandHeader.Feedback](../command_header/commandheader-feedback.md) |  |  |
| joint_velocity_command_feedback | [JointVelocityCommand.Feedback](../basic_command/jointvelocitycommand-feedback.md) | oneof feedback |  |
| se2_velocity_command_feedback | [SE2VelocityCommand.Feedback](../basic_command/se2velocitycommand-feedback.md) | oneof feedback |  |
