(rb-api-waitforcontrolreadyrequest)=
# WaitForControlReadyRequest

- Source proto: [`rb/api/control_manager.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/control_manager.proto) (rby1-sdk v0.10.1)

Request of the `WaitForControlReady` RPC of [ControlManagerService](../control_manager_service/controlmanagerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| timeout | [google.protobuf.Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration) |  |  |
