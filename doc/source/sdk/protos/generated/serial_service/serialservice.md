(rb-api-serialservice)=
# SerialService

- Source proto: [`rb/api/serial_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/serial_service.proto) (rby1-sdk v0.10.1)

Lists the serial devices on the robot PC (RPC) and opens a two-way stream to one of them.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSerialDeviceList | [GetSerialDeviceListRequest](../serial/getserialdevicelistrequest.md) | [GetSerialDeviceListResponse](../serial/getserialdevicelistresponse.md) |  |
| OpenSerialStream | [OpenSerialStreamRequest](../serial/openserialstreamrequest.md) stream | [OpenSerialStreamResponse](../serial/openserialstreamresponse.md) stream |  |
