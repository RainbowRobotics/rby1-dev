# SetSystemTimeRequest

- Source proto: `rb/api/system.proto`

Request to set system time.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md#rb-api-requestheader) |  |  |
| utc_time | [google.protobuf.Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp) |  |  |
| time_zone | [string](../scalar-value-types.md#scalar-value-types) |  | https://en.wikipedia.org/wiki/List_of_tz_database_time_zones |
