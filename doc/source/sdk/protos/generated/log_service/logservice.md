(rb-api-logservice)=
# LogService

- Source proto: [`rb/api/log_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/log_service.proto) (rby1-sdk v0.10.1)

Reads the robot program log (last entries or a live stream), sets the log level and lists fault logs.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetLastLog | [GetLastLogRequest](../log/getlastlogrequest.md) | [GetLastLogResponse](../log/getlastlogresponse.md) |  |
| GetLogStream | [GetLogStreamRequest](../log/getlogstreamrequest.md) | [GetLogStreamResponse](../log/getlogstreamresponse.md) stream |  |
| SetLogLevel | [SetLogLevelRequest](../log/setloglevelrequest.md) | [SetLogLevelResponse](../log/setloglevelresponse.md) |  |
| GetFaultLogList | [GetFaultLogListRequest](../log/getfaultloglistrequest.md) | [GetFaultLogListResponse](../log/getfaultloglistresponse.md) |  |
