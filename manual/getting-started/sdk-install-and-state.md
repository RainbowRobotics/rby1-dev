# SDK Installation

Install the Python SDK (`rby1-sdk`) on your PC, connect to the robot and read its state.
This page does not move the robot.

## Requirements

| Item | Supported (rby1-sdk 0.10.1 wheels on PyPI) |
| --- | --- |
| Python | 3.10, 3.11, 3.12, 3.13 |
| Linux | x86_64 and aarch64 with glibc 2.35 or later (for example Ubuntu 22.04 or 24.04) |
| Windows | 64-bit (x64) |
| macOS | Apple Silicon (arm64), macOS 14 or later |

On other platforms (for example Ubuntu 20.04, Intel Macs or Python 3.9), `pip` downloads the source package
and tries to build it, which needs a full C++ tool chain. See [Supported Platforms](supported-platforms.md) for details,
and the [C++ build guide](../sdk/cpp/build-and-link.md) for the C++ SDK.

## Install (Python)

Linux and macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install rby1-sdk==0.10.1
python -c "import rby1_sdk; print(rby1_sdk.__version__)"
```

Windows (PowerShell):

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -U pip
pip install rby1-sdk==0.10.1
python -c "import rby1_sdk; print(rby1_sdk.__version__)"
```

The last command prints the installed SDK version. This site documents rby1-sdk 0.10.1.
`numpy` 2.x is installed with the SDK.

## Connect and read the state

You need the address of the robot PC (RPC). It depends on how your PC reaches the robot:

| How you are connected | Address to use |
| --- | --- |
| Robot hotspot ([Hotspot & Web UI](hotspot-and-webui.md)) | `192.168.12.1:50051` |
| Your Wi‑Fi network ([External Access Point](connect-external-ap.md)) | `<IP shown in the Web UI>:50051` |
| From the user PC (UPC) inside the robot | `192.168.30.1:50051` |

See [Network and Ports](network-and-ports.md) for all addresses and ports.

The model name must match your robot: `"a"` (Model A, two wheels), `"m"` (Model M, four wheels)
or `"ub"` (Model UB, no mobile base).

```python
import rby1_sdk as rby

ADDRESS = "192.168.12.1:50051"  # RPC address and gRPC port (robot hotspot)
MODEL = "a"                     # "a", "m" or "ub": must match the robot

robot = rby.create_robot(ADDRESS, MODEL)
if not robot.connect():
    raise SystemExit(f"Cannot connect to {ADDRESS}")

info = robot.get_robot_info()
# The robot reports its own joint count; a wrong MODEL gives a different count.
if info.degree_of_freedom != robot.model().robot_dof:
    raise SystemExit(f"Wrong model '{MODEL}': the robot has {info.degree_of_freedom} joints")
print("Robot software:", info.version)  # robot_version is deprecated (it holds the model name)

state = robot.get_state()
print("Time:", state.timestamp)
print(f"Battery: {state.battery_state.level_percent:.1f} %, {state.battery_state.voltage:.1f} V")
print("E-Stop:", [emo.state for emo in state.emo_states])
print("Joint positions [rad]:", state.position)
```

`robot.get_state()` returns a `RobotState`. Commonly used fields:

| Field | Content |
| --- | --- |
| `timestamp` | Time of the state |
| `battery_state` | `voltage` [V], `current` [A], `level_percent` [%] |
| `power_states` | State of each power rail |
| `emo_states` | E-Stop state (`Released` or `Pressed`) |
| `position`, `velocity`, `torque`, `current` | Per-joint arrays, `robot.model().robot_dof` long |
| `joint_states` | Per-joint details (`is_ready`, `power_on`, `temperature`, ...) |
| `odometry` | Mobile base pose (SE(2)) |

See [`RobotState_A`](../sdk/python/generated/rby1_sdk.RobotState_A.md) in the Python API reference for the full list
(`RobotState_M` and `RobotState_UB` have the same fields).

::: warning
The SDK examples `03_robot_state.py` and `04_robot_state_stream.py` also print the state, but they
**turn on all power rails** first (`--power '.*'` by default). Run them only when the robot may be powered.
:::

## Next steps

- [First Motion](first-motion.md): move the robot with the SDK examples and test the E-Stop.
- [Examples](../examples/ex.md): all Python and C++ examples.
- [ROS 2](../ros2/index.md) and [Simulation](../simulators/index.md).
- [Connection Troubleshooting](connection-troubleshooting.md) if `connect()` fails.
