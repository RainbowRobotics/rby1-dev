# Power & Battery

## Disconnect the Charger Before Driving the Mobile Base

::: warning CAUTION
If you drive the mobile base while the charger is connected, the base pulls on the charger cable. This can damage the cable and the charging port, and the cable can make people trip.

- Check that the charger is disconnected before you drive the mobile base.
:::

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/disconnect.png')" alt="Charger plug connected to the charging port on the mobile base (left) and the same port after the plug is removed (right)" class="white-bg" style="width:100%">

---
## Do Not Push the Robot While the Power Is Off

::: warning CAUTION
Pushing the robot by hand turns the wheel motors. The motors then generate back EMF (a voltage), which can damage the electronics. The robot is also heavy and is hard to stop once it rolls.

- Do not push the robot while the power is off.
- To move the robot, power it on and drive it. For example, press the RPC hotspot button, connect your phone to the robot's hotspot Wi-Fi with the QR code, and use **Navigation** in the Web UI **Control Panel**. See [Connect to Hotspot & Check Web UI](../getting-started/hotspot-and-webui.md).
:::

<div class="media-grid" style="--cols:3">

<div>

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/hotspot_button.png')" alt="RPC Hotspot button on the backpack panel" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/hotspot_qr.png')" alt="Pressing the hotspot button; the QR code for the hotspot Wi-Fi appears on the backpack display" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/webui_phone.png')" alt="Web UI on a phone showing the Navigation card with the drive joysticks" class="white-bg">

</div>

</div>

---
## Disable the Control Manager Before Changing the Power State

::: warning CAUTION
If you turn off one power line (5V, 12V, 24V or 48V) while the Control Manager is enabled, the Control Manager goes to a major fault (**Major Fault**). The robot can stop in an uncontrolled way, and joints without a brake are not held (see [Operation](operation.md#joints-without-a-brake)).

- Always disable the Control Manager before you turn any power line on or off.
- Then turn the power lines on or off.
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/error.png')" alt="Web UI error messages: power state changed during enable state, Major Fault Reaction Started, Motor Error Occurred" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/major_fault.png')" alt="Web UI status bar showing Control Manager: Major Fault" class="white-bg">

</div>

</div>

You can check the Control Manager state in two places:
- The front LED: blue when the Control Manager is enabled, white when it is idle (disabled), red at a major fault.
- The **Control Manager** status at the top of the Web UI.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/control_manager.png')" alt="Control Manager states and front LED colors: Enabled (blue), Idle (white), Major Fault (red)" class="white-bg" style="width:100%">

---
## Shutdown Order

::: info NOTICE
Turning off power in the wrong order can cause a major fault. Shut down in this order:
:::

1. In the Web UI **Control Panel**, press **ZERO** in the **Samples** card to move the robot to the zero pose. The robot moves: clear the area first.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/zero_pose.png')" alt="Samples card with the ZERO, READY and PACKING buttons and the robot pose for each" class="white-bg" style="width:100%">

2. Press **Disable** in the **Control Manager** card. The front LED changes from blue to white.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/control_manager_disable.png')" alt="Control Manager card with the Disable button; the state changes from Enabled (blue LED) to Idle (white LED)" class="white-bg" style="width:100%">

3. In the **Powers** card, select all power lines (5v, 12v, 24v, 48v) and press **Off**.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/power_off.png')" alt="Powers card with 5v, 12v, 24v and 48v selected and the Off button" class="white-bg" style="width:100%">

---
## Disconnect the Battery for Long-Term Storage

::: info NOTICE
If the robot is not used for a long time, the battery discharges. Disconnect the battery connector to prevent this.
:::

1. Shut down the robot (see [Shutdown Order](#shutdown-order)).
2. Open the front cover to reach the battery connector.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/front_cover.png')" alt="Front cover of the lower body and the two screws that hold it" class="white-bg" style="width:100%">

3. Disconnect the battery connector.

<img :src="$withBase('/images/safety_and_precautions/power_and_battery/power_disconnect.png')" alt="Pulling apart the yellow battery connector behind the front cover" class="white-bg" style="width:100%">

4. Before you use the robot again, reconnect the battery connector, then power on.

---
## Battery

::: warning CAUTION
The robot uses a lithium-ion battery pack (see [Battery](../hardware/battery.md)). A damaged lithium-ion battery can overheat or catch fire.

- If the battery pack is damaged, swollen, hot or smells unusual, stop using the robot, disconnect the battery connector if you can do it safely, and contact Rainbow Robotics support (see [Support](../support.md)).
:::
