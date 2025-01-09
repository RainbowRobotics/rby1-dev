---
outline: deep
---

# Access Information
This section provides details about how to connect to the Robot PC from the User PC, including network addresses, credentials, and Web UI access.

## Network Information:

* Robot PC IP Address (User PC to Robot PC): 192.168.30.1

* Robot PC IP Address (Hotspot Connection: `192.168.12.1`  
  - Hotspot SSID: `RBY1`  
  - Hotspot Password: The password can be viewed after connecting via QR code.  
    > :key: **Connecting via QR Code**
    > 1. Press the **HOTSPOT button** on the top of the robot's backpack to activate the hotspot.  
    > 2. A QR code will be displayed; scan it to automatically connect to the network.  
    > - The hotspot will remain active **only while the HOTSPOT button is pressed**.  
    > - Ensure the button is not pressed again during robot operation, as this will deactivate the hotspot and disrupt communication with the robot.  

## Web UI Access
* User PC(UPC) to Robot PC(RPC): 192.168.30.1:5173
* Hotspot Connection: 192.168.12.1:5173

## Access Credentials
- User PC Username: `nvidia`  
- User PC Password: `nvidia`  

> :warning: **Note**  
> The default credentials are standard for Nvidia Jetson devices.  

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

- **Left LiDAR IP Address:** `192.168.30.10`  
- **Right LiDAR IP Address:** `192.168.30.11`  

Use these addresses to connect to the respective LiDAR sensors for data collection and monitoring.

### Additional Information

- The LiDAR sensors used in this system are **LakiBeam 1L**.  
- For more details and documentation, visit the official site:  
  [RichBeam LakiBeam 1L Documentation](https://www.richbeam.com/en/download)  

### Example Code

A simple example code for printing LiDAR data is available at the following repository:  
[RainbowRobotics/lakibeam-1l-test](https://github.com/RainbowRobotics/lakibeam-1l-test.git)  

This example demonstrates basic usage of the LakiBeam 1L LiDAR sensors.  