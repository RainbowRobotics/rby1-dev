(rb-api-mobilitycommand-request)=
# MobilityCommand.Request

- Source proto: [`rb/api/mobility_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/mobility_command.proto) (rby1-sdk v0.10.1)

Request part of [MobilityCommand](mobilitycommand.md).

Only one field of the `command` oneof can be set at a time: `joint_velocity_command`, `se2_velocity_command`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_velocity_command | [JointVelocityCommand.Request](../basic_command/jointvelocitycommand-request.md) | oneof command |  |
| se2_velocity_command | [SE2VelocityCommand.Request](../basic_command/se2velocitycommand-request.md) | oneof command |  |
