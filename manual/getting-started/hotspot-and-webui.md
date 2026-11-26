# Hotspot & Web UI

The simplest way to connect to the robot the first time is its **hotspot**: your laptop joins the Wi‑Fi network
of the robot PC (RPC) and opens the Web UI in a browser. In the Web UI you check the robot status,
power it on and move it to the zero pose.

::: warning
The steps below power the robot, enable its servos and move it to the zero pose.
Read [E‑Stop Basics](estop-basics.md) first, keep the E‑Stop or the remote controller in your hand,
and clear the space around the robot.
:::

## Connect to the hotspot

1. Check that the E-Stop button is released.

2. Turn on the RPC with its power switch on the top of the robot
   (see [Electrical Part](../hardware/electrical_part.md#robot-pc-rpc)), and wait until it has started.

3. Press the **HOTSPOT** button on top of the backpack. It stays pressed in, and the hotspot runs while it is pressed in.
   If the button is already pressed in, press it once to release it, then press it again.

   The display shows `Please wait ...`, then a QR code when the hotspot is ready.

   <div class="media-grid" style="--cols:2">

   <div>

   <img :src="$withBase('/images/safety_and_precautions/power_and_battery/hotspot_button.png')" alt="HOTSPOT button on the backpack" class="white-bg">

   </div>

   <div>

   <img :src="$withBase('/images/safety_and_precautions/power_and_battery/hotspot_qr.png')" alt="QR code on the backpack display" class="white-bg">

   </div>

   </div>

4. On your laptop or phone, scan the QR code, or join the Wi‑Fi network by hand:
   - SSID: `RBY1`
   - Password: `RBY1@@@@`

   These are the factory defaults. While the hotspot runs, the RPC is disconnected from any other Wi‑Fi network.

5. Open the Web UI in a browser: `http://192.168.12.1:5173`. The dashboard shows the robot status
   (power, battery, E-Stop, joint angles and logs).

   <img :src="$withBase('/images/getting-started/webui_dashboard.png')" alt="dashboard" class="center white-bg" style="width:800px">

::: tip Change the hotspot password
Everyone who knows the default password can join the hotspot and control the robot.
After the first setup, set your own SSID and password in **Settings** → **RPC Hotspot** (robot software 0.11.0 and later).
On older versions, set the parameters `hotspot.ssid` and `hotspot.password`, for example with
`robot.set_parameter("hotspot.password", "\"<new password>\"")` in the SDK.
Use 8 to 63 characters, without spaces. The new values are used the next time the hotspot starts.
:::

## Unpacking wizard

From the left menu, select **Unpacking** to open the setup wizard.

<img :src="$withBase('/images/getting-started/webui_sidebar.png')" alt="sidebar" class="center white-bg" style="width:800px">

- **Step 0**

  Unpack the robot completely and connect the charger, so the battery does not run low.

  <img :src="$withBase('/images/getting-started/webui_unpacking_step0.png')" alt="step0" class="center white-bg" style="width:800px">

- **Step 1. Turn Power On**

  Click **Power On** to supply power to the robot.
  The system bar at the top shows **Power** in blue when the power is on.
  If it shows **Power** in orange, the E-Stop is pressed: release it and try again.

  <img :src="$withBase('/images/getting-started/webui_unpacking_step1.png')" alt="step1" class="center white-bg" style="width:800px">

- **Step 2. Active Servo**

  Click **Servo On**. This turns on the joint motors of all joints defined in the model and starts homing.
  Wait until homing has finished before you continue.
  If some joints (for example the head or the wheels) are removed, turn on the servos only for the remaining
  joints in the **Control Panel**.

  <img :src="$withBase('/images/getting-started/webui_unpacking_step2.png')" alt="step2" class="center white-bg" style="width:800px">

- **Step 3. Enable Control Manager**

  Click **Enable(Unlimit)** so that the robot can execute commands. The state changes to **Enabled**.
  If the state shows **Fault**, press **Reset** and try again.

  ::: warning
  The Unpacking wizard enables the Control Manager only in **Unlimit** mode.
  Unlimit skips the joint operating range check, so the robot can move outside its joint limits.
  Use it only for unpacking, and switch to the standard mode in the last step.
  :::

  <img :src="$withBase('/images/getting-started/webui_unpacking_step3.png')" alt="step3" class="center white-bg" style="width:800px">

- **Step 4. Move to Zero Pose**

  Click **Zero** to send the robot to the zero pose.
  The robot moves slowly to a standing position.
  Keep the remote controller in your hand and make sure the path is clear.
  To cut the power immediately, press button 1 on the remote controller or the E-Stop button.
  **CANCEL CONTROL** at the top of the screen cancels the motion without cutting the power; the motion does not resume.

  ::: info
  The wizard text calls this button **SOFT STOP**. The button at the top of the screen is labelled **CANCEL CONTROL**.
  :::

  <img :src="$withBase('/images/getting-started/webui_unpacking_step4.png')" alt="step4" class="center white-bg" style="width:800px">

- **Finish**: switch to the standard mode (required)

  The robot is still in **Unlimit** mode after Step 4.
  Press **Disable**, then press **Enable** on this page to switch the Control Manager to the standard mode,
  in which the joint operating range is checked.
  Do this before you use the SDK, teleoperation or ROS 2.

  <img :src="$withBase('/images/getting-started/webui_unpacking_step5.png')" alt="finish" class="center white-bg" style="width:800px">

## Web UI at a glance

| Place | Content |
| --- | --- |
| System bar (top line) | **Power**, **Servo**, **Control Manager** and **Control** states |
| Top bar | **CANCEL CONTROL** and **ESTOP** (see [E‑Stop Basics](estop-basics.md#ways-to-stop-the-robot)) |
| **Dashboard** | Uptime, CPU, memory, current, battery and E-Stop (**EMO**) cards, and the log |
| **Robot Viewer** | 3D view of the robot |
| **Control Panel** | Power, servos, brakes, Control Manager, tool flange power and simple motions |
| **Settings** | Parameters, **RPC WiFi Settings**, **RPC Hotspot**, **UPC Network (NAT)** and **Utilities** (log downloads). Some cards exist only in newer robot software. |
| **Unpacking** | The setup wizard above |

## Next

- [External Access Point](connect-external-ap.md): move the robot onto your Wi‑Fi network.
- [Network and Ports](network-and-ports.md): all addresses and ports.
- [Connection Troubleshooting](connection-troubleshooting.md) if the hotspot or the Web UI does not work.

---

Verified against: robot core `core/robots/rby1a/robot_app.cpp` (hotspot button: on while pressed in, off when released;
display shows `Please wait ...`, then the QR code; Wi‑Fi disconnected while the hotspot runs),
`core/robots/rby1a/parameters.h` (`hotspot.ssid` `RBY1`, `hotspot.password` `RBY1@@@@`);
Web UI (core v0.11.0) `UnpackingStepper.vue`, `NavigatorDrawer.vue`, `SystemBar.vue`,
`DashboardComponents/RpcStatusCards.vue`, `pages/control-pannel.vue`, `pages/settings.vue`,
`SettingComponents/Hotspot.vue` (added in v0.11.0), `WiFi.vue`, `PortForward.vue`, `Utilities.vue`;
rby1-sdk v0.10.1 `python/robot.cpp` (`set_parameter` example for `hotspot.ssid`).
