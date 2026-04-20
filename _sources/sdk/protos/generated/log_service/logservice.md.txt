(rb-api-logservice)=
# LogService

- Source proto: `rb/api/log_service.proto`

gRPC service for log.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLastLog | [GetLastLogRequest](../log/getlastlogrequest.md) | [GetLastLogResponse](../log/getlastlogresponse.md) |  |
| GetLogStream | [GetLogStreamRequest](../log/getlogstreamrequest.md) | [GetLogStreamResponse](../log/getlogstreamresponse.md) stream |  |
| SetLogLevel | [SetLogLevelRequest](../log/setloglevelrequest.md) | [SetLogLevelResponse](../log/setloglevelresponse.md) |  |
| GetFaultLogList | [GetFaultLogListRequest](../log/getfaultloglistrequest.md) | [GetFaultLogListResponse](../log/getfaultloglistresponse.md) |  |
