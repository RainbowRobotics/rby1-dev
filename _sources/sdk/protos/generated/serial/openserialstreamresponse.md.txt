(rb-api-openserialstreamresponse)=
# OpenSerialStreamResponse

- Source proto: `rb/api/serial.proto`

Response for open serial stream.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| connect_result | [SerialConnectionStatus](serialconnectionstatus.md) |  |  |
| write_result | [SerialWriteResult](serialwriteresult.md) |  |  |
| read_data | [bytes](../scalar-value-types.md) |  |  |
