(rb-api-downloadfileresponse)=
# DownloadFileResponse

- Source proto: [`rb/api/file.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/file.proto) (rby1-sdk v0.10.1)

Response of the `DownloadFile` RPC of [FileService](../file_service/fileservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| file_content | [bytes](../scalar-value-types.md) |  |  |
