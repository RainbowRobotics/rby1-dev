# LEDService

- Source proto: `rb/api/led_service.proto`

Service for controlling LED behavior

| Method Name | Request Type | Response Type | Description |
| ----------- | ------------ | ------------- | ------------|
| SetLEDColor | [SetLEDColorRequest](./setledcolorrequest.md#rb-api-setledcolorrequest) | [SetLEDColorResponse](./setledcolorresponse.md#rb-api-setledcolorresponse) | Sets the LED color and (optionally) its blinking behavior. If blinking is true, the LED blinks at &#39;blinking_freq&#39; for &#39;duration&#39;. Otherwise, the LED remains in the requested color for &#39;duration&#39;. |
