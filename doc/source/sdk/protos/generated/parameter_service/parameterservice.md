(rb-api-parameterservice)=
# ParameterService

- Source proto: [`rb/api/parameter_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/parameter_service.proto) (rby1-sdk v0.10.1)

Reads, sets and resets the robot parameters.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| FactoryResetAllParameters | [FactoryResetAllParametersRequest](../parameter/factoryresetallparametersrequest.md) | [FactoryResetAllParametersResponse](../parameter/factoryresetallparametersresponse.md) |  |
| FactoryResetParameter | [FactoryResetParameterRequest](../parameter/factoryresetparameterrequest.md) | [FactoryResetParameterResponse](../parameter/factoryresetparameterresponse.md) |  |
| ResetAllParameters | [ResetAllParametersRequest](../parameter/resetallparametersrequest.md) | [ResetAllParametersResponse](../parameter/resetallparametersresponse.md) |  |
| ResetParameter | [ResetParameterRequest](../parameter/resetparameterrequest.md) | [ResetParameterResponse](../parameter/resetparameterresponse.md) |  |
| GetParameter | [GetParameterRequest](../parameter/getparameterrequest.md) | [GetParameterResponse](../parameter/getparameterresponse.md) |  |
| SetParameter | [SetParameterRequest](../parameter/setparameterrequest.md) | [SetParameterResponse](../parameter/setparameterresponse.md) |  |
| GetParameterList | [GetParameterListRequest](../parameter/getparameterlistrequest.md) | [GetParameterListResponse](../parameter/getparameterlistresponse.md) |  |
| ResetAllParametersToDefault | [ResetAllParametersToDefaultRequest](../parameter/resetallparameterstodefaultrequest.md) | [ResetAllParametersToDefaultResponse](../parameter/resetallparameterstodefaultresponse.md) | **Deprecated.** Does the same as FactoryResetAllParameters; use that instead. |
| ResetParameterToDefault | [ResetParameterToDefaultRequest](../parameter/resetparametertodefaultrequest.md) | [ResetParameterToDefaultResponse](../parameter/resetparametertodefaultresponse.md) | **Deprecated.** Does the same as FactoryResetParameter; use that instead. |
