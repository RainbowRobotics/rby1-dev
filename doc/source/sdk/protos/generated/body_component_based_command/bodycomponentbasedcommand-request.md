# BodyComponentBasedCommand.Request

- Source proto: `rb/api/body_component_based_command.proto`

Request payload for BodyComponentBasedCommand.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md#rb-api-commandheader-request) |  |  |
| right_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md#rb-api-armcommand-request) |  |  |
| left_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md#rb-api-armcommand-request) |  |  |
| torso_command | [TorsoCommand.Request](../torso_command/torsocommand-request.md#rb-api-torsocommand-request) |  |  |
