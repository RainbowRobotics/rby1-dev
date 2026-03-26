# JointCommandRequest

- Source proto: `rb/api/power.proto`

Request to joint command.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md#rb-api-requestheader) |  | Request header |
| name | [string](../scalar-value-types.md#scalar-value-types) |  | Motor ID |
| command | [JointCommandRequest.Command](jointcommandrequest-command.md#rb-api-jointcommandrequest-command) |  |  |
