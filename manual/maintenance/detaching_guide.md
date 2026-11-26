# Parts Detaching

This page shows how to detach and attach the arm, the wrist pitch (WP) module, the gripper and the F/T sensor.

::: danger Before you detach any part
- Shut down the robot in the right order and turn all power lines off (see [Shutdown Order](../precautions/power_and_battery.md#shutdown-order)). Then turn off the robot PC (RPC) and the user PC (UPC).
- For work inside the body, also disconnect the battery connector (see [Disconnect the Battery for Long-Term Storage](../precautions/power_and_battery.md#disconnect-the-battery-for-long-term-storage)).
- An arm weighs about 11 kg (see [Weight](../hardware/overview.md#weight)). Support the arm before you remove its bolts. Do this work with two people.
- Contact the support team before you send a part back.
:::

The procedures on this page do not list bolt torques or connector order. Ask the support team (<a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>) for these values before you reassemble a part.

---
## Detach the Arm

If an arm has a problem, the support team may ask you to detach it and send it in.

1. Shut down the robot and turn off the power (see above).
2. Support the arm.
3. Remove the 4 bolts and take off the rear cover.
4. Detach the arm as shown below.

<img :src="$withBase('/images/maintenance/detaching_guide/arm_disassembly.gif')" alt="Removing the rear cover bolts and detaching the arm" class="center white-bg" style="width:600px">

---
## Detach and Attach the Wrist Pitch (WP) Module

If the tool flange connector is damaged, replace it with these guides:

- Detaching guide (PPT): <a href="https://rainbowco-my.sharepoint.com/:p:/g/personal/rby_support_rainbow-robotics_com/EV9ih8p56CdHtK1ZUf5ZpYcBwIg_-GVEBDv0yzINKbhutw?e=FaCXJI" target="_blank" rel="noopener noreferrer">Download</a>
- Attaching guide (PPT): <a href="https://rainbowco-my.sharepoint.com/:p:/g/personal/rby_support_rainbow-robotics_com/EYrC4bDHOZlOkO8H0td6bjYBaF1IW-Uxkz4hrANThqOdug?e=UhRfBm" target="_blank" rel="noopener noreferrer">Download</a>

---
## Detach the F/T Sensor and Gripper

Use these steps to replace the F/T sensor and the gripper with your own devices.
Model M v1.3 has no F/T sensor (see [Hardware Versions](../sdk/models/hardware-versions.md)).

Tools: 3 mm L-wrench and an extension bar.

<img :src="$withBase('/images/maintenance/detaching_guide/l-wrench-and-extension-bar.jpg')" alt="3 mm L-wrench and extension bar" class="center white-bg" style="width:600px">

1. Disconnect the F/T sensor and gripper connector as shown below.

   <img :src="$withBase('/images/maintenance/detaching_guide/ft_gripper.gif')" alt="Disconnecting the F/T sensor and gripper connector" class="center white-bg" style="width:600px">

2. Push the F/T sensor cable slightly aside to make room for the wrench.

   <img :src="$withBase('/images/maintenance/detaching_guide/ft_dis1.png')" alt="F/T sensor cable pushed aside" class="center white-bg" style="width:600px">

3. Loosen the bolt at the F/T sensor cable outlet with the L-wrench and the extension bar.

   <img :src="$withBase('/images/maintenance/detaching_guide/ft_dis2.png')" alt="Loosening the bolt at the cable outlet" class="center white-bg" style="width:600px">

4. Loosen the other 3 bolts with the L-wrench.

   <img :src="$withBase('/images/maintenance/detaching_guide/ft_dis3.png')" alt="Loosening the other three bolts" class="center white-bg" style="width:600px">

5. Remove all 4 bolts and pull the gripper off gently.

   <img :src="$withBase('/images/maintenance/detaching_guide/ft_dis4.png')" alt="Removing the gripper" class="center white-bg" style="width:600px">

After you attach a new F/T sensor or gripper, set the F/T sensor zero (see [FT Sensor Initialization](../rpc_management_tools/ft_sensor_initialize.md)).

---
## More Resources

The [Manual and Technical Documents](https://rainbowco-my.sharepoint.com/:f:/g/personal/support_rainbow-robotics_com/IgB3yw9hTL55QotVBfymVVPpAejrOE0QDoPCiQ3ETL3Kng0?e=rP8rA9) folder has more maintenance material: manuals, technical documents and 3D model files. Check the files for your robot model before you start.
