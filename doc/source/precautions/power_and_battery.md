# Power & Battery

## Precautions
<br>

### ⚠️Before moving the mobile, make sure to check that the charger is disconnected.
<br>

```{image} ../_static/images/saftey_and_precautions/power_and_battery/disconnect.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```


---
### ⚠️Disconnect Battery connector During Long-Term Inactivity

- Open the front cover to access the battery connector.

```{image} ../_static/images/saftey_and_precautions/power_and_battery/front_cover.png
    :alt: charger1
    :width: 100%
    :class: white_bg
```

- If the robot is not used for an extended period, disconnect the battery connector to prevent battery discharge.

```{image} ../_static/images/saftey_and_precautions/power_and_battery/power_disconnect.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```

- Before using the robot again, ensure that the battery connector is properly reconnected before powering on.


---
### ⚠️Back EMF Risk When Moving Robot (Power OFF)


- If you move the mobile robot by applying force manually, back EMF may be generated.
- Avoid applying force to move the robot when the power is OFF.
- We recommend pressing the RPC hotspot button, connecting to RBY1 Wi-Fi via the QR code, and controlling mobile movement with your phone. ({doc}`Hotspot And Web UI </getting-started/hotspot-and-webui>`)

`````{grid} 3
:gutter: 3

````{grid-item}
```{image} ../_static/images/saftey_and_precautions/power_and_battery/hotspot_button.png
    :alt: charger1
    :width: 100%
    :align: center
    :class: white_bg equal-size-image
```
````

````{grid-item}
```{image} ../_static/images/saftey_and_precautions/power_and_battery/hotspot_qr.png
    :alt: charger2
    :width: 100%
    :align: center
    :class: white_bg equal-size-image
```
````

````{grid-item}
```{image} ../_static/images/saftey_and_precautions/power_and_battery/webui_phone.png
    :alt: charger2
    :width: 100%
    :align: center
    :class: white_bg equal-size-image
```
````
`````

---
### ⚠️When finishing operation, move the robot to the Zero Pose, then disable the Control Manager and power off the system.


- Move to zero pose in the Web UI.

```{image} ../_static/images/saftey_and_precautions/power_and_battery/zero_pose.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```
<br>


- Perform Control Manager disable; when disabled, the front LED changes from blue to white.

```{image} ../_static/images/saftey_and_precautions/power_and_battery/control_manager_disable.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```
<br>


- Turn off all power (5V, 12V, 24V, 48V).

```{image} ../_static/images/saftey_and_precautions/power_and_battery/power_off.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```


---
### ⚠️Before changing the robot power state, ensure that the Control Manager is disabled.


- When the Control Manager is Enabled (i.e., all power rails are ON), turning OFF only a specific power line (such as 5V, 12V, 24V, or 48V) may cause system instability or a major fault.

`````{grid} 2
:gutter: 2

````{grid-item}
```{image} ../_static/images/saftey_and_precautions/power_and_battery/error.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```
````

````{grid-item}
```{image} ../_static/images/saftey_and_precautions/power_and_battery/major_fault.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```
````
`````

- Always disable the Control Manager before changing any power state.
- After disabling the Control Manager, proceed to safely turn ON/OFF the required power lines.


```{important}
- You can check whether Control Manager is disabled from the front LED.
- You can also verify it from the Control Manager status at the top of the Web UI.
```

```{image} ../_static/images/saftey_and_precautions/power_and_battery/control_manager.png
    :alt: charger2
    :width: 100%
    :class: white_bg
```
