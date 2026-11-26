# External Access Point

Move the robot onto your own network, so that your PCs reach it without the hotspot.

- The **robot PC (RPC)** joins your Wi‑Fi network (access point, AP). The SDK, the Web UI and ROS 2 then use
  the RPC IP address on that network.
- The **user PC (UPC)** has its own Ethernet port for internet access (see [Wired (UPC)](#wired-upc)).

See [Network and Ports](network-and-ports.md) for all addresses.

## Wi‑Fi (RPC)

Connect to the robot hotspot first ([Hotspot & Web UI](hotspot-and-webui.md)).

1. In the Web UI, open **Settings**.

<img :src="$withBase('/images/getting-started/wifi1.png')" alt="Settings menu" class="center white-bg" style="width:800px">

2. Find the **RPC WiFi Settings** card with the **Scan WiFi** button.

<img :src="$withBase('/images/getting-started/wifi2.png')" alt="RPC WiFi Settings card" class="center white-bg" style="width:800px">

3. Click **Scan WiFi** and wait for the list of networks.

<img :src="$withBase('/images/getting-started/wifi3.png')" alt="Scanned networks" class="center white-bg" style="width:800px">

4. Click **Connect** next to your network. Enter the password and choose **IP Assignment**:
   **DHCP** (address from your network) or **Static IP** (enter **IP Address**, **Gateway** and **DNS**).
   Click **Connect**.

<img :src="$withBase('/images/getting-started/wifi4.png')" alt="Connect dialog" class="center white-bg" style="width:800px">

5. Release the **HOTSPOT** button. The hotspot stops and the RPC joins your network.
   The display on the backpack shows the network name and the RPC IP address.

6. Join your laptop to the same network and open `http://<RPC IP>:5173`.
   **Current WiFi** and **IP** on the **RPC WiFi Settings** card show the connection.

<img :src="$withBase('/images/getting-started/wifi5.png')" alt="Connected network and IP address" class="center white-bg" style="width:800px">

Use this IP address for the SDK: `<RPC IP>:50051`. With DHCP, the address can change;
ask your network administrator to reserve an address for the robot, or use **Static IP**.

## Wired (UPC)

Connect an Ethernet cable to the UPC port to give the UPC internet access.

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/getting-started/wire1.jpg')" alt="UPC Ethernet port" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/getting-started/wire2.jpg')" alt="Ethernet cable connected" class="white-bg">

</div>

</div>

From robot software 0.11.0, the UPC can also use the RPC Wi‑Fi connection for internet access, and you can reach
the UPC through port forwarding on the RPC. See [Network and Ports](network-and-ports.md#reaching-the-upc-from-your-network).

## Next

[SDK Installation](sdk-install-and-state.md): install the Python SDK and read the robot state.
