(rb-api-bodycomponentbasedcommand-request)=
# BodyComponentBasedCommand.Request

- Source proto: `rb/api/body_component_based_command.proto`

Request payload for BodyComponentBasedCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| right_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md) |  |  |
| left_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md) |  |  |
| torso_command | [TorsoCommand.Request](../torso_command/torsocommand-request.md) |  |  |
