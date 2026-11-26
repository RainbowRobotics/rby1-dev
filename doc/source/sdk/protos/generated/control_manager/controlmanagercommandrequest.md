(rb-api-controlmanagercommandrequest)=
# ControlManagerCommandRequest

- Source proto: [`rb/api/control_manager.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/control_manager.proto) (rby1-sdk v0.10.1)

Request of the `ControlManagerCommand` RPC of [ControlManagerService](../control_manager_service/controlmanagerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| command | [ControlManagerCommandRequest.Command](controlmanagercommandrequest-command.md) |  |  |
| unlimited_mode_enabled | [google.protobuf.BoolValue](https://protobuf.dev/reference/protobuf/google.protobuf/#boolvalue) |  |  |
