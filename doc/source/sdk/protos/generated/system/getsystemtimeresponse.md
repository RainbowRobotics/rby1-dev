(rb-api-getsystemtimeresponse)=
# GetSystemTimeResponse

- Source proto: [`rb/api/system.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/system.proto) (rby1-sdk v0.10.1)

Response of the `GetSystemTime` RPC of [SystemService](../system_service/systemservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md) |  |  |
| utc_time | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| time_zone | [string](../scalar-value-types.md) |  | https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |
| local_time | [string](../scalar-value-types.md) |  |  |
