# Network and Ports

RB-Y1 has two computers:

- **Robot PC (RPC)**: runs the robot software (core), the gRPC server for the SDK and the Web UI.
- **User PC (UPC)**: a computer for your own programs (for example the leader arm and the gripper).
  See [Electrical Part](../hardware/electrical_part.md#user-pc-upc-and-robot-pc-rpc).

Your PC talks to the RPC. The SDK, ROS 2 driver and RPC tools all use the RPC address and gRPC port 50051.

## Addresses

| Network | RPC address | Notes |
| --- | --- | --- |
| Robot hotspot (`RBY1`) | `192.168.12.1` | Your PC gets an address in `192.168.12.0/24`. See [Hotspot & Web UI](hotspot-and-webui.md). |
| Your Wi‑Fi network (external AP) | Given by your network (DHCP) or set by you (static) | Shown in the Web UI (**Settings** → **RPC WiFi Settings** → **IP**) and on the display on the backpack. See [External Access Point](connect-external-ap.md). |
| Internal wired network (RPC ↔ UPC) | `192.168.30.1` | Subnet `192.168.30.0/24`, wired inside the robot. The UPC is on this subnet (the Web UI port-forwarding example uses `192.168.30.2`). |

The RPC has one Wi‑Fi interface. It works either as the hotspot or as a client of your Wi‑Fi network, not both:

- Pressing the **HOTSPOT** button disconnects the RPC from your Wi‑Fi network.
- Releasing the button stops the hotspot, and the RPC reconnects to the saved Wi‑Fi network.

## Ports on the RPC

| Port | Service | Used by |
| --- | --- | --- |
| 50051 (TCP) | gRPC server of the robot software | SDK (`rby.create_robot("<RPC address>:50051", ...)`), ROS 2 driver, RPC tools |
| 5173 (TCP) | Web UI | Browser: `http://<RPC address>:5173` |
| 8000 (TCP) | Web UI back end (HTTP and WebSocket) | The Web UI page; your firewall must allow it too |
| 22 (TCP) | SSH | Maintenance |

Examples:

```text
Hotspot:         Web UI http://192.168.12.1:5173     SDK 192.168.12.1:50051
Your network:    Web UI http://<RPC IP>:5173         SDK <RPC IP>:50051
On the UPC:      SDK 192.168.30.1:50051
```

## Reaching the UPC from your network

The UPC is only on the internal network. From robot software 0.11.0, the Web UI has a **UPC Network (NAT)** card
under **Settings**:

- **Port forwarding**: forwards a port of the RPC Wi‑Fi address to a port on the UPC.
  The **Add SSH (2222 → 22)** button adds a rule for SSH; then connect with `ssh -p 2222 <user>@<RPC IP>`.
  The ports above (22, 50051, 5173, 8000) and ports 8001 and 8888 are reserved and cannot be forwarded.
- **Share RPC WiFi internet with UPC**: lets the UPC reach the internet through the RPC Wi‑Fi connection.

Alternatively, connect an Ethernet cable to the UPC for internet access ([External Access Point](connect-external-ap.md#wired-upc)).

## Simulator

The simulator runs the same robot software and gRPC server. Use the address of the computer that runs the
simulator container with port 50051, for example `127.0.0.1:50051`. See [Simulation](../simulators/index.md).

---

Verified against: robot core `core/main.cpp` (gRPC on `0.0.0.0:50051`), `core/base/system.h` (bridge `br0`
`192.168.30.1/24`), `core/base/hotspot.h` and `core/robots/rby1a/robot_app.cpp` (hotspot with `create_ap`,
Wi‑Fi disconnected while the hotspot runs, reconnected after it stops, SSID and IP sent to the display),
`core/robots/rby1a/parameters.h` (hotspot SSID); `rby1-web/docker-compose.web.yaml` (Web UI on 5173, back end on
uvicorn port 8000), `rby1-web/rby1-frontend/src/config/apiConfig.js` (API port 8000),
`rby1-web/rby1-frontend/src/components/SettingComponents/PortForward.vue`, `Hotspot.vue`, `WiFi.vue`
(core v0.11.0); `rby1-web/system_files/rby1-portfwd` (reserved ports, default UPC target `192.168.30.2`);
rby1-sdk v0.10.1 `examples/python/*.py` (usage address `192.168.30.1:50051`).
