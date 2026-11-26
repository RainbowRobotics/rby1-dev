(rb-api-fileservice)=
# FileService

- Source proto: [`rb/api/file_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/file_service.proto) (rby1-sdk v0.10.1)

Downloads a file from the robot PC (RPC) as a stream of chunks.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| DownloadFile | [DownloadFileRequest](../file/downloadfilerequest.md) | [DownloadFileResponse](../file/downloadfileresponse.md) stream |  |
