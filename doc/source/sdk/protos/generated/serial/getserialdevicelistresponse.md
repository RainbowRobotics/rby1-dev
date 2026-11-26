(rb-api-getserialdevicelistresponse)=
# GetSerialDeviceListResponse

- Source proto: [`rb/api/serial.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/serial.proto) (rby1-sdk v0.10.1)

Response of the `GetSerialDeviceList` RPC of [SerialService](../serial_service/serialservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| devices | [SerialDeviceInfo](serialdeviceinfo.md) | repeated |  |
