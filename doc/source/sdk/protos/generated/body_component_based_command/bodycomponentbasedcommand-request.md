(rb-api-bodycomponentbasedcommand-request)=
# BodyComponentBasedCommand.Request

- Source proto: [`rb/api/body_component_based_command.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/body_component_based_command.proto) (rby1-sdk v0.10.1)

Request part of [BodyComponentBasedCommand](bodycomponentbasedcommand.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| command_header | [CommandHeader.Request](../command_header/commandheader-request.md) |  |  |
| right_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md) |  |  |
| left_arm_command | [ArmCommand.Request](../arm_command/armcommand-request.md) |  |  |
| torso_command | [TorsoCommand.Request](../torso_command/torsocommand-request.md) |  |  |
