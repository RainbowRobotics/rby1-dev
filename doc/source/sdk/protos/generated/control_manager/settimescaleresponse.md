(rb-api-settimescaleresponse)=
# SetTimeScaleResponse

- Source proto: [`rb/api/control_manager.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/control_manager.proto) (rby1-sdk v0.10.1)

Response of the `SetTimeScale` RPC of [ControlManagerService](../control_manager_service/controlmanagerservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  | Response header |
| current_time_scale | [double](../scalar-value-types.md) |  |  |
