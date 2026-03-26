# GetSystemTimeResponse

- Source proto: `rb/api/system.proto`

Response for get system time.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| response_header | [ResponseHeader](../header/responseheader.md#rb-api-responseheader) |  |  |
| utc_time | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| time_zone | [string](../scalar-value-types.md#scalar-value-types) |  | https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |
| local_time | [string](../scalar-value-types.md#scalar-value-types) |  |  |
