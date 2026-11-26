(rb-api-wifinetwork)=
# WifiNetwork

- Source proto: [`rb/api/system.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/system.proto) (rby1-sdk v0.10.1)

A Wi-Fi network found by a scan: SSID, signal strength and whether it is secured.

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| ssid | [string](../scalar-value-types.md) |  |  |
| signal_strength | [int32](../scalar-value-types.md) |  | dBm |
| secured | [bool](../scalar-value-types.md) |  |  |
