# LogService

- Source proto: `rb/api/log_service.proto`

gRPC service for log.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLastLog | [GetLastLogRequest](../log/getlastlogrequest.md#rb-api-getlastlogrequest) | [GetLastLogResponse](../log/getlastlogresponse.md#rb-api-getlastlogresponse) |  |
| GetLogStream | [GetLogStreamRequest](../log/getlogstreamrequest.md#rb-api-getlogstreamrequest) | [GetLogStreamResponse](../log/getlogstreamresponse.md#rb-api-getlogstreamresponse) stream |  |
| SetLogLevel | [SetLogLevelRequest](../log/setloglevelrequest.md#rb-api-setloglevelrequest) | [SetLogLevelResponse](../log/setloglevelresponse.md#rb-api-setloglevelresponse) |  |
| GetFaultLogList | [GetFaultLogListRequest](../log/getfaultloglistrequest.md#rb-api-getfaultloglistrequest) | [GetFaultLogListResponse](../log/getfaultloglistresponse.md#rb-api-getfaultloglistresponse) |  |
