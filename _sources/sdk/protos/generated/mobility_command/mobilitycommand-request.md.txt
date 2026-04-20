(rb-api-mobilitycommand-request)=
# MobilityCommand.Request

- Source proto: `rb/api/mobility_command.proto`

Request payload for MobilityCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| joint_velocity_command | [JointVelocityCommand.Request](../basic_command/jointvelocitycommand-request.md) |  |  |
| se2_velocity_command | [SE2VelocityCommand.Request](../basic_command/se2velocitycommand-request.md) |  |  |
