# User PC (UPC)

RB-Y1 has two computers. The **robot PC (RPC)** runs the robot software, the gRPC server and the [Web UI](web-ui.md).
The **user PC (UPC)** is for your own programs. You can use it, replace it, or leave it off and control the robot from your own PC.

## Hardware

- **Computer**: NVIDIA Jetson AGX Orin (64 GB module) on an AverMedia D315 carrier board (ARM64).
- **Ports**: 2 USB, 2 Ethernet and 1 HDMI. See [Electrical Part](../hardware/electrical_part.md#user-pc-upc-and-robot-pc-rpc).
- **Power**: its own power switch on the top of the body.

## What runs on the UPC

| Program | Why on the UPC |
| --- | --- |
| Your SDK programs | Short, wired link to the RPC: use the robot address `192.168.30.1:50051`. |
| [Leader arm](../options/leader_arm.md) programs and [teleoperation](../options/teleoperation.md) | The leader arm connects to the UPC by USB (device `/dev/rby1_leader_arm`). |
| [Gripper](../options/gripper.md) programs | The gripper communication module connects to the UPC (device `/dev/rby1_gripper`). |
| [ROS 2 driver](../ros2/index.md) and your ROS 2 nodes | Run next to the robot; see [UPC Topic Bridge](../ros2/ros2_driver/upc_topic_bridge.md) to use them from another PC. |

The SDK on the UPC has the module `rby1_sdk.upc` for these devices (`LeaderArm`, `initialize_device`, the device names above).
Install the SDK on the UPC as on any Linux PC: see [SDK Installation](../getting-started/sdk-install-and-state.md).

::: warning
Programs on the UPC move the robot like programs on any other PC. Keep the E-Stop within reach when you start them,
and stop them before you leave the robot.
:::

## Network

| Network | Address | Notes |
| --- | --- | --- |
| Internal wired network (inside the robot) | UPC `192.168.30.2` (default), RPC `192.168.30.1` | Subnet `192.168.30.0/24`. The UPC reaches the robot software at `192.168.30.1:50051`. |
| UPC Ethernet port | Given by your network | Plug a cable into the UPC port for internet access. See [External Access Point](../getting-started/connect-external-ap.md#wired-upc). |

The UPC is not on the robot hotspot or on your Wi‑Fi network by itself. Check the link from the UPC with `ping 192.168.30.1`.

## Reach the UPC

- **Keyboard and monitor**: connect them to the USB and HDMI ports of the UPC.
- **Ethernet**: connect the UPC port to your network and use the address your network gives it.
- **Through the RPC** (robot software 0.11.0 and later): in the Web UI, **Settings** → **UPC Network (NAT)**:
  - **Port forwarding**: **Add SSH (2222 → 22)** adds a rule. Then connect from a PC on the robot hotspot or your Wi‑Fi network with
    `ssh -p 2222 <user>@<RPC address>`, where `<user>` is the account on your UPC.
    New connections are limited to 10 per minute per rule; **Allow from** limits the clients that may connect.
  - **Share RPC WiFi internet with UPC**: lets the UPC use the RPC Wi‑Fi connection for internet access.
    On the UPC, set the default route and a DNS server, for example `sudo ip route add default via 192.168.30.1`.

  The reserved ports 22, 50051, 5173, 8000, 8001 and 8888 of the RPC cannot be forwarded.
  See [Network and Ports](../getting-started/network-and-ports.md#reaching-the-upc-from-your-network).

---

Verified against: rby1-sdk v0.10.1 `include/rby1-sdk/upc/device.h` (`/dev/rby1_gripper`, `/dev/rby1_leader_arm`), `python/upc.cpp`,
`python/rby1_sdk/upc.py`, `examples/python/*.py` (address `192.168.30.1:50051`); robot core `core/base/system.h` (`192.168.30.1/24`),
Web UI v0.11.0 `rby1-web/rby1-frontend/src/components/SettingComponents/PortForward.vue` (SSH rule, rate limit, internet sharing, default route),
`rby1-web/system_files/rby1-portfwd` (reserved ports, default UPC target `192.168.30.2`); manual pages Electrical Part (UPC hardware) and
UPC Topic Bridge.
