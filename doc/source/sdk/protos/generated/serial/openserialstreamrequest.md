(rb-api-openserialstreamrequest)=
# OpenSerialStreamRequest

- Source proto: [`rb/api/serial.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/serial.proto) (rby1-sdk v0.10.1)

Request of the `OpenSerialStream` RPC of [SerialService](../serial_service/serialservice.md).

Only one field of the `payload` oneof can be set at a time: `connect`, `write`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| connect | [SerialOpenRequest](serialopenrequest.md) | oneof payload |  |
| write | [SerialWriteRequest](serialwriterequest.md) | oneof payload |  |
