(rb-api-systemservice)=
# SystemService

- Source proto: [`rb/api/system_service.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/system_service.proto) (rby1-sdk v0.10.1)

System settings of the robot PC (RPC): system time, battery level and configuration, network reset and Wi-Fi.

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| GetSystemTime | [GetSystemTimeRequest](../system/getsystemtimerequest.md) | [GetSystemTimeResponse](../system/getsystemtimeresponse.md) |  |
| SetSystemTime | [SetSystemTimeRequest](../system/setsystemtimerequest.md) | [SetSystemTimeResponse](../system/setsystemtimeresponse.md) |  |
| SetBatteryLevel | [SetBatteryLevelRequest](../system/setbatterylevelrequest.md) | [SetBatteryLevelResponse](../system/setbatterylevelresponse.md) |  |
| SetBatteryConfig | [SetBatteryConfigRequest](../system/setbatteryconfigrequest.md) | [SetBatteryConfigResponse](../system/setbatteryconfigresponse.md) |  |
| ResetBatteryConfig | [ResetBatteryConfigRequest](../system/resetbatteryconfigrequest.md) | [ResetBatteryConfigResponse](../system/resetbatteryconfigresponse.md) |  |
| ResetNetworkSetting | [ResetNetworkSettingRequest](../system/resetnetworksettingrequest.md) | [ResetNetworkSettingResponse](../system/resetnetworksettingresponse.md) |  |
| ScanWifi | [ScanWifiRequest](../system/scanwifirequest.md) | [ScanWifiResponse](../system/scanwifiresponse.md) |  |
| ConnectWifi | [ConnectWifiRequest](../system/connectwifirequest.md) | [ConnectWifiResponse](../system/connectwifiresponse.md) |  |
| DisconnectWifi | [DisconnectWifiRequest](../system/disconnectwifirequest.md) | [DisconnectWifiResponse](../system/disconnectwifiresponse.md) |  |
| GetWifiStatus | [GetWifiStatusRequest](../system/getwifistatusrequest.md) | [GetWifiStatusResponse](../system/getwifistatusresponse.md) |  |
