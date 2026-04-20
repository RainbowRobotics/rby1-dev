(rb-api-ledservice)=
# LEDService

- Source proto: `rb/api/led_service.proto`

gRPC service for led.

Service for controlling LED behavior

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| SetLEDColor | [SetLEDColorRequest](../led/setledcolorrequest.md) | [SetLEDColorResponse](../led/setledcolorresponse.md) | Sets the LED color and (optionally) its blinking behavior. If blinking is true, the LED blinks at &#39;blinking_freq&#39; for &#39;duration&#39;. Otherwise, the LED remains in the requested color for &#39;duration&#39;. |
