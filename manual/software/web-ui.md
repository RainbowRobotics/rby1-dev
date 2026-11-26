# Web UI

The Web UI is a browser interface that runs on the robot PC (RPC). Use it to check the robot status, turn power and servos on,
enable the Control Manager, move joints, and change settings, without writing code.

Open it at `http://<RPC address>:5173`, for example `http://192.168.12.1:5173` on the robot hotspot.
The first connection is described in [Hotspot & Web UI](../getting-started/hotspot-and-webui.md); all addresses and ports are in
[Network and Ports](../getting-started/network-and-ports.md).

This page describes the Web UI of robot software 0.11.0. Older versions have fewer cards.

::: danger WARNING
Many buttons in the Web UI power the robot, turn on the servos, release brakes or move joints and the mobile base.
Read [E‑Stop Basics](../getting-started/estop-basics.md) first, keep the hardware E-Stop or the remote controller within reach,
and clear the space around the robot.

The **ESTOP** button in the Web UI is a software stop: it cancels the running command and turns off all power rails over the network.
It does not replace the hardware E-Stop, and it does not work when the network connection is lost.
:::

## Layout

| Place | Content |
| --- | --- |
| System bar (top line) | **Power**, **Servo**, **Control Manager** and **Control** states |
| Top bar, **CANCEL CONTROL** | Cancels the running command (`cancel_control()`). The power stays on and the robot holds its position. |
| Top bar, **ESTOP** | Cancels the running command and turns off all power rails (software stop, see the warning above). |
| Top bar, ⋮ menu | **All Power On**, **All Power Off**, **All Servo On**, **Control Enable**, **Control Disable**, **Control Reset** |
| Left menu (☰) | **Dashboard**, **Robot Viewer**, **Control Panel**, **Settings**, **Unpacking**, and links to this manual and the SDK on GitHub |

**All Servo On** shows a warning first: turning on the servos rotates the wrists. Check that nothing can collide before you press **Proceed**.

## Dashboard

The home page of the Web UI.

- **Status cards**: uptime, CPU, memory and disk of the RPC, battery load current, battery level and the E-Stop (**EMO**) state.
- **Joints** table: for every joint its index and name, error flags, position (°), velocity (°/s), temperature (°C), current (A),
  torque (N·m) and the reference position (°). Hover over a flag letter to see its meaning:

  | Flag | Meaning |
  | --- | --- |
  | **I** | Actuator not ready (Servo On failed) |
  | **J** | Mechanical jamming detected |
  | **C** | Current exceeds threshold |
  | **B** | Large deviation from reference |
  | **N** | Invalid reference value |

- **FT Sensor / Tool Flange**: force/torque sensor values, tool flange output voltage and the direct teaching button of the right and left arm.
- **Log**: the latest messages of the robot software.
- **Versions** at the bottom: RPC (robot software) version, SDK version, **Model** and **Model Version** (hardware version, see [Hardware Versions](../sdk/models/hardware-versions.md)).

The Web UI shows angles in degrees. The SDK uses radians (see [Units and Frames](units-and-frames.md)).

## Robot Viewer

A 3D view of the robot model that follows the joint positions of the real robot.

## Control Panel

| Card | What it does |
| --- | --- |
| **Powers** | Select power rails (for example `5v`, `12v`, `24v`, `48v`) and turn them **On** or **Off**. |
| **Servos** | Select joint groups (Torso, Right Arm, Left Arm, Head, Wheel) or single joints and turn their servos **On**. |
| **Control Manager** | **Enable**, **Reset** (after a fault), **Disable**, and **Unlimit** (enable even when a joint is outside its range). |
| **Navigation** | Two on-screen joysticks drive the mobile base: linear velocity up to 0.2 m/s and rotation up to 10°/s. **Turbo** doubles both (0.4 m/s, 20°/s) and always turns on **Smoothing**; **Smoothing** softens acceleration. |
| **Samples** | Move the robot to the **ZERO**, **READY** or **PACKING** pose. |
| **Tool Flange Power** | Turn the tool flange output of the right and/or left arm on at **12V** or **24V**, or off. |
| **Brake** | **ENGAGE** or **RELEASE** the brakes of selected joints. Release asks for confirmation. |
| **Send Position** | Per-joint table with the measured position, the reference and jog buttons. **Jog Step (deg)** sets the step size. |

::: warning
- **Unlimit** skips the joint range check at enable, so the Control Manager is enabled even when a joint is outside its limits.
  Whether commands still respect the joint limits in this mode is not verified on a robot. Use it only to bring a joint back into its range
  (for example during unpacking), then **Disable** and **Enable** again in the standard mode.
- **RELEASE** on the **Brake** card can let the selected joints fall under gravity. Support the robot first.
- **Navigation**, **Samples** and **Send Position** move the robot. Keep the area clear and the E-Stop within reach.
:::

## Settings

| Card | What it does |
| --- | --- |
| **RPC WiFi Settings** | Scan for Wi‑Fi networks and connect the RPC to one, with DHCP or a static IP. Shows the current network, gateway and band. **Preferred band** sets the parameter `wifi.band`. See [External Access Point](../getting-started/connect-external-ap.md). |
| **RPC Hotspot** | SSID, password (8 to 63 characters), band, channel and width of the robot hotspot. The settings apply the next time the HOTSPOT button is pressed. If 5 GHz is refused, the hotspot falls back to 2.4 GHz and the card shows the reason. |
| **UPC Network (NAT)** | **Port forwarding** from a port of the RPC Wi‑Fi address to the user PC (UPC), and **Share RPC WiFi internet with UPC**. See [User PC (UPC)](upc.md#reach-the-upc). |
| **Utilities** | **Download Recent Logs** (last 10) or **Download All Logs**, and the **Updater** instructions with **Release Page** and **Download Updater**. See [RPC Updater](../rpc_management_tools/rpc_updater.md). |
| **Parameters** | The robot parameters with their current values (see below). |

### Parameters

The **Parameters** card lists every robot parameter with its current value. Type a new value in **Target Value** and press **Set**.
Type numbers as numbers and arrays as `[a, b, c]`; text values can be typed without quotes. Values are saved permanently.
The meaning, unit and range of each parameter are in the [Parameter Reference](../sdk/controllers/generated/parameter.md).

| Button | Effect |
| --- | --- |
| **Export** | Downloads a file `rby1-config-<model>-<date>.json` with all parameters, the port-forwarding rules and the custom robot models (URDF). |
| **Import** | Loads an exported file, shows a preview of every change, and applies only the items you select. |
| **Default Reset** | Restores the parameters from the database: discards values that were set without saving. |
| **Factory Reset** | Sets all parameters to their factory defaults. |

Notes on **Import**:

- The file must come from the same robot model (A, M or UB). `robot_model_name` is never imported.
- Robot-specific values (`battery_config`, `gravity`, `hotspot.ssid`, `hotspot.password`, `model_name`) are not selected by default
  when the file comes from another robot.
- `model_name`, `boot.power_on_target` and `major_fault_power_off_target` take effect after the robot software restarts; the preview tells you.
- If a parameter or model fails to import, the parameters and models already applied are restored.
  The port-forwarding rules are applied last and are reported separately; they are not restored.

::: warning
The exported file contains the hotspot password. Store and share it like a password.
:::

## Unpacking

A step-by-step wizard for the first start: power on, servo on, enable the Control Manager and move to the zero pose.
See [Hotspot & Web UI](../getting-started/hotspot-and-webui.md#unpacking-wizard).

## Other services on the RPC

- **JupyterLab**: older robot software had a JupyterLab on the RPC. It is disabled from robot software 0.10.7; port 8888 stays reserved.
  Run your own notebooks on the UPC or on your PC with the SDK instead.
- **Port 8001** serves a service console for Rainbow Robotics service engineers. It is not part of the user Web UI.

---

Verified against: robot core v0.11.0 Web UI `rby1-web/rby1-frontend/src/components/NavigatorDrawer.vue` (menu, top bar, ⋮ menu, servo warning),
`pages/index.vue`, `pages/viewer.vue`, `pages/control-pannel.vue`, `pages/settings.vue`, `DashboardComponents/RpcStatusCards.vue`,
`RobotStatusTable.vue` (columns and flags), `SensorsCard.vue`, `ControlComponents/Power.vue`, `Servo.vue`, `ControlManager.vue`, `Joystick.vue`
(stick range 0.4 m/s, π/18 rad/s, turbo), `TemplatePosture.vue`, `Toolflange.vue`, `Break.vue`, `SendPosition.vue`, `SettingComponents/WiFi.vue`, `Hotspot.vue`,
`PortForward.vue`, `Utilities.vue`, `ParamTables.vue` (`parseTarget`), `ConfigImportDialog.vue`; back end `rby1_web/core/routers/params.py`, `rby1-web/rby1-backend/rby1_web/core/routers/power.py`
(`estop`: cancel control and power off `.*`; `soft_stop`: cancel control), `rby1_web/operator/routers/config.py`, `config_backup.py`
(identity, robot-specific and restart-required parameters; `apply`: parameters and models restored on failure, port forward written last),
`rby1_web/core/routers/joystick.py` (normal and turbo scales, turbo forces smoothing); `rby1-web/docker-compose.web.yaml` (ports 5173, 8000, 8001);
`CHANGELOG.md` (v0.10.7: JupyterLab disabled); robot core `core/control/control_manager.cpp` (`Enable`: unlimited mode skips the joint range check at enable).
