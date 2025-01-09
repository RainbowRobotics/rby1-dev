---
outline: deep
---

# Access Information
This section provides details about how to connect to the Robot PC from the User PC, including network addresses, credentials, and Web UI access.

## Network Information:

* Robot PC IP Address (User PC to Robot PC): 192.168.30.1
* Robot PC IP Address (Hotspot Connection): 192.168.12.1
    * Hotspot SSID: RBY1
    * Hotspot Password: [Provided separately to licensed users]

    > :warning: If you are a licensed user and do not know the default password, please contact rby.support@rainbow-robotics.com for assistance. We will verify your license and provide the necessary information.

    > :key: Press the HOTSPOT button on the top of the robot's backpack for the hotspot to function. You can also connect via the QR code displayed when the button is pressed.

## Web UI Access
* User PC to Robot PC: 192.168.30.1:5173
* Hotspot Connection: 192.168.12.1:5173

## Access Credentials
* User PC Username: [Provided separately to licensed users]
* User PC Password: [Provided separately to licensed users]
> :warning: If you are a licensed user and do not know the default password, please contact rby.support@rainbow-robotics.com for assistance. We will verify your license and provide the necessary information.


## Command Information
* Command Port: 50051 (Use this port to send commands to the Robot PC.)

## Sending Commands to the Robot

### From the User PC (UPC)
1. **Direct Command via Code:**
   - Send commands to the Robot PC at `192.168.30.1:50051` from the UPC by writing code that interfaces with the robot.
   
2. **SSH Connection:**
   - You can also SSH into the UPC and send commands to the Robot PC at `192.168.30.1:50051`.  
   >:bulb: The UPC only supports **wired connections**, so if you need a wireless solution, you'll need to implement it manually.

<figure>
    <img src="/images/using-included-pc.png" alt="missing" style="width:80%;margin:auto;" />
    <figcaption style="text-align: center;">[ (Option 1) Using included PC as UPC ]</figcaption>
</figure>

### From Another PC(Your own PC)
There are two methods to send commands to the Robot PC from another PC:

1. **Using Hotspot:**
   - Connect the other PC to the same Wi-Fi as the Robot PC via the **HOTSPOT**.
   - Send commands to `192.168.12.1:50051`.

2. **Using a Separate Wi-Fi Network:**  
   - Connect the Robot PC and your PC to a different Wi-Fi network.
   - Assign the Robot PC to that Wi-Fi network.
   - Send commands to the **Robot PC's IP address** on the same network, followed by `:50051` for the command port.  
   - More detailed instructions on this method will be provided later.

<figure>
    <img src="/images/using-your-own-pc.png" alt="missing" style="width:100%;margin:auto;" />
    <figcaption style="text-align: center;">[ (Option 2) Using your own PC as UPC ]</figcaption>
</figure>

## LiDAR Information
You can access the LiDAR sensors via the following IP addresses:

* **Left LiDAR IP Address:** 192.168.30.10
* **Right LiDAR IP Address:** 192.168.30.11

Use these addresses to connect to the respective LiDAR sensors for data collection and monitoring.
