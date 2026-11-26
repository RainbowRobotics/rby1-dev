(rb-api-openserialstreamresponse)=
# OpenSerialStreamResponse

- Source proto: [`rb/api/serial.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/serial.proto) (rby1-sdk v0.10.1)

Response of the `OpenSerialStream` RPC of [SerialService](../serial_service/serialservice.md).

Only one field of the `payload` oneof can be set at a time: `connect_result`, `write_result`, `read_data`.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| connect_result | [SerialConnectionStatus](serialconnectionstatus.md) | oneof payload |  |
| write_result | [SerialWriteResult](serialwriteresult.md) | oneof payload |  |
| read_data | [bytes](../scalar-value-types.md) | oneof payload |  |
