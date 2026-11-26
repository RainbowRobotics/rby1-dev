(rb-api-commonerror)=
# CommonError

- Source proto: [`rb/api/header.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/header.proto) (rby1-sdk v0.10.1)

Error code and message, set in a ResponseHeader when the request failed.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| code | [CommonError.Code](commonerror-code.md) |  | Error code |
| message | [string](../scalar-value-types.md) |  | Human-readable error message |
