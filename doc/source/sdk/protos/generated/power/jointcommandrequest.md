(rb-api-jointcommandrequest)=
# JointCommandRequest

- Source proto: `rb/api/power.proto`

Request to joint command.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  | Request header |
| name | [string](../scalar-value-types.md) |  | Motor ID |
| command | [JointCommandRequest.Command](jointcommandrequest-command.md) |  |  |
