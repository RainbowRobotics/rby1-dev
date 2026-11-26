(rb-api-gamepad)=
# Gamepad

- Source proto: [`rb/api/gamepad.proto`](https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/protos/rb/api/gamepad.proto) (rby1-sdk v0.10.1)

Gamepad button and joystick values. The UploadGamepadData RPC takes a stream of these messages.

Request of the `UploadGamepadData` RPC of [GamepadService](../gamepad_service/gamepadservice.md).

| Field | Type | Label | Description |
| ----- | ---- | ----- | ----------- |
| buttons | [bool](../scalar-value-types.md) | repeated |  |
| joystick | [double](../scalar-value-types.md) | repeated |  |
