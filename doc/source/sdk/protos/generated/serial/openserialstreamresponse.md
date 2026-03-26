# OpenSerialStreamResponse

- Source proto: `rb/api/serial.proto`

Response for open serial stream.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md#rb-api-responseheader) |  |  |
| connect_result | [SerialConnectionStatus](serialconnectionstatus.md#rb-api-serialconnectionstatus) |  |  |
| write_result | [SerialWriteResult](serialwriteresult.md#rb-api-serialwriteresult) |  |  |
| read_data | [bytes](../scalar-value-types.md#scalar-value-types) |  |  |
