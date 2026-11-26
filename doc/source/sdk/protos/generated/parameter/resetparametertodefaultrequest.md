(rb-api-resetparametertodefaultrequest)=
# ResetParameterToDefaultRequest

- Source proto: [`rb/api/parameter.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/parameter.proto) (rby1-sdk v0.10.1)

Request of the `ResetParameterToDefault` RPC of [ParameterService](../parameter_service/parameterservice.md).

```{note}
Deprecated. Use FactoryResetParameter instead.
```

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| request_header | [RequestHeader](../header/requestheader.md) |  |  |
| name | [string](../scalar-value-types.md) |  |  |
