# Unboxing

This page guides you through unboxing and preparing your robot for its first use.
Read [E‑Stop Basics](estop-basics.md) first.

## Included Items

- RB-Y1 robot: torso and two arms, with a mobile base on Model A and Model M (model-specific)
- Charger
- 2x terminal board
- Remote controller (wireless E-Stop)

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/getting-started/package/charger.png')" alt="Charger" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/getting-started/package/emo_remote_control.png')" alt="Remote controller (wireless E-Stop)" class="white-bg">

</div>

</div>

## Connecting the Power

For shipping, the connection between the battery and the PDU is disconnected to prevent battery discharge.
Before operating the robot, the first step is to reconnect the power cables.

### Before you connect

- Press the E-Stop button.
- Check that the robot PC (RPC) and user PC (UPC) power switches are off
  (see [Electrical Part](../hardware/electrical_part.md#user-pc-upc-and-robot-pc-rpc)).
- Keep tools and metal parts away from the open connectors.

### Open Front Body Cover

Unscrew the two bolts near the head to open the body's front cover.

<img :src="$withBase('/images/getting-started/unboxing_body_cover.png')" alt="Open the front body cover" class="center white-bg" style="width:400px">

### Connect the Cables

Connect the two connectors as shown below.
Make sure the connector orientation is correct before mating; do not force the connection if it does not align.
Push each connector fully home in one movement.

::: warning Caution
A small spark may occur when the battery connector is mated.
:::

<img :src="$withBase('/images/getting-started/unboxing_connector.png')" alt="connect the cables" class="center white-bg" style="width:400px">

Close the front cover, then release the E-Stop button before you power on.

### Connect the Charger

The robot normally operates on battery power. It can also be powered while connected to the charger.
Keep the charger connected during the first setup, so the battery does not run low.

::: warning
Disconnect the charger before you drive the mobile base. See [Power & Battery](../precautions/power_and_battery.md).
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/getting-started/charger1.jpg')" alt="Charger connected to the robot" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/getting-started/charger2.jpg')" alt="Charger connector" class="white-bg">

</div>

</div>

## Next

[Hotspot & Web UI](hotspot-and-webui.md): power on the robot and run the setup wizard.
For battery handling and long-term storage, see [Power & Battery](../precautions/power_and_battery.md).
