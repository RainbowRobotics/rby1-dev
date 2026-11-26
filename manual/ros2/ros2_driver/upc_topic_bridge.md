# UPC Topic Bridge

How a PC on the robot PC (RPC)'s wireless network (its AP) uses the topics, services and actions of the ROS 2 nodes on the user PC (UPC).

The UPC (192.168.30.2) sits on the robot's internal network, behind the RPC (192.168.30.1).
A PC on the RPC's wireless network reaches the UPC only through the RPC's port forwarding, for example SSH through RPC port 2222.
ROS 2 (DDS) does not pass this: its discovery is multicast, and its traffic uses many UDP ports.

`zenoh-bridge-ros2dds` carries it over one TCP port instead. One bridge runs on the UPC and one on your PC; each joins the ROS 2 domain on its side,
and the two connect through one forwarded port, 7449. Every topic, service and action of that domain then appears on the other side.

## Requirements

- **RPC 0.11.0 or later**: its Web UI has the port forwarding rules used below. Update the RPC with the [RPC Updater](../../rpc_management_tools/rpc_updater.md).
- **The same `ROS_DOMAIN_ID` on both sides**, set in `~/.bashrc`. This page uses 77. Use a number from 2 to 101 that nothing else on the UPC or the network uses (not 0 or 1: the UPC's own software uses them).
- **`zenoh-bridge-ros2dds` 1.10.2 on both sides**, the same version.
- **Port 7449 on the UPC.** Ports 7447 and 7448 are taken by the bridges that come with the UPC's software.

::: warning Anyone who reaches the port can command the robot
With the bridge running, any client on the RPC's wireless network that reaches port 7449 joins the domain and can call the driver's services and actions,
which move the robot. To admit only your PC, set **Allow from (CIDR)** in the forwarding rule to its address.
:::

## 1. RPC: forward port 7449

1. Open the RPC Web UI in a browser.
2. Go to **Settings** (section *UPC Network (NAT)*, *Port forwarding*).
3. Click **ADD RULE** and fill the new row:

   | Name | RPC port | Proto | UPC IP | UPC port | Allow from (CIDR) |
   |---|---|---|---|---|---|
   | `ros2_bridge` | `7449` | `tcp` | `192.168.30.2` | `7449` | your PC's address, e.g. `192.168.12.34/32` (empty: any client) |

4. Click **APPLY**. The rule shows in *Active*.

## 2. UPC: run the bridge

Type these commands on the UPC. From your PC, log in through RPC port 2222 (`<robot_ip>`: the RPC's address on its wireless network):

```bash
ssh -p 2222 nvidia@<robot_ip>
```

Set the domain once:

```bash
echo 'export ROS_DOMAIN_ID=77' >> ~/.bashrc
source ~/.bashrc
```

Get the standalone bridge for the UPC's CPU (aarch64) from the [zenoh-plugin-ros2dds 1.10.2 release](https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases/tag/1.10.2):

```bash
mkdir -p ~/zenoh_bridge && cd ~/zenoh_bridge
wget https://github.com/eclipse-zenoh/zenoh-plugin-ros2dds/releases/download/1.10.2/zenoh-plugin-ros2dds-1.10.2-aarch64-unknown-linux-gnu-standalone.zip
unzip zenoh-plugin-ros2dds-1.10.2-aarch64-unknown-linux-gnu-standalone.zip
```

Write its settings, `~/zenoh_bridge/upc_bridge.json5`:

```bash
cat > ~/zenoh_bridge/upc_bridge.json5 <<'EOF'
{
  plugins: {
    ros2dds: {
      deny: {
        publishers: ["/rosout", "/parameter_events"],
        subscribers: ["/rosout", "/parameter_events"],
      },
    },
  },
  mode: "router",
  listen: { endpoints: ["tcp/0.0.0.0:7449"] },
  scouting: { multicast: { enabled: false } },
}
EOF
```

| Setting | Meaning |
|---|---|
| (no `domain`) | The bridge joins the domain of `ROS_DOMAIN_ID`, as the nodes do |
| `deny` | What is not carried. Everything else of the domain is carried both ways. `allow` instead carries only what it lists |
| `mode`, `listen` | The UPC's bridge waits for your PC's bridge on TCP 7449 |
| `scouting` | Off: it does not look for other bridges on the network |

Run it and leave it running (Ctrl+C stops it):

```bash
cd ~/zenoh_bridge && ROS_DISTRO=humble ./zenoh-bridge-ros2dds -c upc_bridge.json5
```

It prints `Zenoh can be reached at: tcp/192.168.30.2:7449`.

## 3. Your PC: connect to the UPC

Set the same domain:

```bash
echo 'export ROS_DOMAIN_ID=77' >> ~/.bashrc
source ~/.bashrc
```

Run the bridge from its Docker image (the standalone build needs glibc 2.38, newer than Ubuntu 22.04's), after the UPC's bridge is running:

```bash
docker run --rm -it --init --net host -e ROS_DISTRO=humble -e ROS_DOMAIN_ID \
  eclipse/zenoh-bridge-ros2dds:1.10.2 client -e tcp/<robot_ip>:7449 --no-multicast-scouting
```

| Argument | Meaning |
|---|---|
| `--init` | Lets Ctrl+C stop it |
| `--net host` | The bridge joins the PC's own network, where its ROS 2 nodes are |
| `-e ROS_DISTRO=humble` | The ROS 2 version of the nodes on this PC |
| `-e ROS_DOMAIN_ID` | Hands this terminal's `ROS_DOMAIN_ID` to the container |
| `-e tcp/<robot_ip>:7449` | The forwarded port on the RPC |

It prints `New ROS 2 bridge detected` once it reaches the UPC's bridge.

## 4. Check the connection

```bash
# UPC
ros2 topic pub /bridge_hello std_msgs/msg/String "{data: hello from UPC}"
# your PC
ros2 topic echo /bridge_hello std_msgs/msg/String
```

Then the same the other way. `ros2 node list` on your PC shows the bridge (`/zenoh_bridge_ros2dds`) rather than the UPC's nodes.

## Tips

- **Same domain in every terminal.** A terminal without `ROS_DOMAIN_ID` runs its nodes, and a bridge, in domain 0. Check with `echo $ROS_DOMAIN_ID` before you start anything.
- **Carry less.** Replace `deny` with `allow` to carry only what it lists (regular expressions), for example `allow: { publishers: ["/chatter", "/tf_static"] },`.
  The kinds: `publishers`, `subscribers`, `service_servers`, `service_clients`, `action_servers`, `action_clients`.
- **Nodes on Jazzy.** One bridge carries one domain of one ROS 2 version. For Jazzy nodes, run a second pair with another domain and port (e.g. 7450, with its own forwarding rule) and `ROS_DISTRO=jazzy`.

Verified against: rby1-ros2 v1.0.0 `Doc/manual/08_upc_topic_bridge.md`, README (ROS domain). Not run here: the commands come from that manual.
