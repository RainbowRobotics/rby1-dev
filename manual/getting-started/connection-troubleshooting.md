# Connection Troubleshooting

Common problems during the first steps, and what to check. Addresses and ports are listed in
[Network and Ports](network-and-ports.md).

## Cannot join the hotspot

- Check that the **HOTSPOT** button on the backpack stays pressed in. The hotspot stops when the button is released.
- Wait a few seconds after pressing it: the display on the backpack shows `Please wait ...`, then a QR code
  when the hotspot is ready. If it shows `Error`, release the button and press it again.
- Use the SSID and password set for your robot. The factory default is SSID `RBY1`, password `RBY1@@@@`;
  they may have been changed in **Settings** → **RPC Hotspot**.

## Cannot open the Web UI

- Use `http://`, not `https://`, and port 5173: `http://192.168.12.1:5173` on the hotspot,
  `http://<RPC IP>:5173` on your network.
- On your network, read the RPC IP on the display on the backpack, or join the hotspot and open
  **Settings** → **RPC WiFi Settings**.
- Your PC must reach both port 5173 (page) and port 8000 (data). If the page loads but shows no data,
  check the firewall and proxy settings of your PC and network.
- Make sure your PC is on the same network as the robot: on the hotspot, your PC has an address in `192.168.12.0/24`.

## SDK `connect()` returns `False`

- Check the address and the port: `<RPC address>:50051`.
- Test that the port is reachable:

  ```bash
  # Linux / macOS
  nc -vz 192.168.12.1 50051
  ```

  ```powershell
  # Windows PowerShell
  Test-NetConnection 192.168.12.1 -Port 50051
  ```

- If the port is not reachable but the Web UI works, check the firewall between your PC and the robot.
- Check that the virtual environment with `rby1-sdk` is active: `python -c "import rby1_sdk; print(rby1_sdk.__version__)"`.

## Connected, but commands fail

- **Wrong model**: the model name in `create_robot(address, model)` must match the robot (`"a"`, `"m"` or `"ub"`).
  Compare `robot.get_robot_info().degree_of_freedom` with `robot.model().robot_dof`; they must be equal.
- **Power on fails**: the E-Stop is pressed. In the Web UI the system bar shows **Power** in orange, and the log
  shows `EMO Error: Please check EMO Switch`. Release the E-Stop. See [E‑Stop Basics](estop-basics.md).
- **Control Manager does not enable**: see [Faults](#faults) below.

## Faults

The Control Manager state is shown in the Web UI system bar, on the LED strip
([LED States](../software/robot_main_program.md#led-states-led-strip-state)) and in the SDK
(`robot.get_control_manager_state().state`).

| State | What happened | What the robot does | Recovery |
| --- | --- | --- | --- |
| `MinorFault` | A command could not be executed, or the hardware was not ready for commands | Stops the commands and holds the current position; power stays on | Find the cause in the log, then **Control Reset** and **Control Enable** |
| `MajorFault` | Lost robot state, a motor or power error, or a power rail changed while enabled (for example the E-Stop) | Turns off the 48 V power and the rails set in the `major_fault_power_off_target` parameter (all by default), and saves a fault log | Remove the cause, release the E-Stop, **Control Reset**, power on, servo on, **Control Enable** |

`23_zero_pose.py` and the other SDK examples that use `initialize_robot()` reset a fault automatically.
Do not reset a fault repeatedly without finding its cause.
See [Fault Diagnosis](../sdk/trobuleshooting/fault-diagnosis.md) for all causes, the fault log format and the recovery steps,
and [SDK Troubleshooting](../sdk/trobuleshooting/index.md) for more SDK connection problems.

## Logs

| Log | How to get it |
| --- | --- |
| Recent log messages | Web UI dashboard **Logs** panel (**FULL LOG** for more), or the SDK: `robot.get_last_log(20)` (example `15_log.py`), or stream them (`16_log_stream.py`) |
| Fault logs (`fault-<time>.csv`, about one minute of robot state before a Major Fault) | SDK: `robot.get_fault_log_list()` and `robot.download_file(...)` (example `17_fault_log.py`) |
| All logs on the RPC | Web UI **Settings** → **Utilities** → **Log Downloads**, or the `log_backup` tool. See [Log Backup](../rpc_management_tools/log_backup.md). |

When you report a problem, send:

1. The robot model and hardware version, and the robot software version (`robot.get_robot_info()`).
2. The SDK version (`rby1_sdk.__version__`) and your OS.
3. What you did and what happened, with the time.
4. The logs from **Log Downloads** and the fault log, if there is one.

See [Error Reporting](../sdk/trobuleshooting/generated/error_reporting.md) for where to send it.

## FAQ

**What is the first-run order?**
Read [E‑Stop Basics](estop-basics.md), then follow [Unboxing](unboxing.md), [Hotspot & Web UI](hotspot-and-webui.md),
[External Access Point](connect-external-ap.md), [SDK Installation](sdk-install-and-state.md) and
[First Motion](first-motion.md).

**Can I start over Wi‑Fi?**
Yes. The first connection uses the robot hotspot. After that, move the robot onto your Wi‑Fi network
([External Access Point](connect-external-ap.md)).

**Which port does the SDK use?**
50051, on the RPC address: for example `192.168.12.1:50051` on the hotspot.

**Where is a complete state example?**
See [SDK Installation](sdk-install-and-state.md#connect-and-read-the-state). The SDK examples
`03_robot_state.py` and `04_robot_state_stream.py` print the full state, but turn on all power rails first.

**The robot clock is wrong.**
Read it with `robot.get_system_time()` and set it with `robot.set_system_time(...)`
(see `13_set_system_time.py`; that example changes the time zone, so edit it before you run it).

---

Verified against: robot core `core/control/control_manager.cpp` (`MinorFault` / `MajorFault` conditions),
`core/robots/robot_app_base.cpp` (Major Fault power off and fault log), `core/robots/rby1a/parameters.h`
(`major_fault_power_off_target`, hotspot defaults), `core/robots/rby1a/robot_app.cpp` (hotspot display messages);
Web UI `UnpackingStepper.vue` (Power orange = E-Stop), `NavigatorDrawer.vue` (Control Enable / Disable / Reset),
`DashboardComponents/RpcStatusCards.vue`, `docker-compose.web.yaml`, `config/apiConfig.js` (port 8000);
rby1-sdk v0.10.1 `examples/python/00_helper.py`, `03_robot_state.py`, `04_robot_state_stream.py`, `13_set_system_time.py`,
`15_log.py`, `16_log_stream.py`, `17_fault_log.py`, `python/robot.cpp`, `python/robot_info.cpp`.
