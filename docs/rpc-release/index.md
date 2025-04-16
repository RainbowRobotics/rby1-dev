---
title: RPC Management Tools
outline: deep
sidebar: false
prev: false
next: false
---
# RPC Management Tools
## How to Update RPC

Please use the provided `updater` program to update your RPC. During the update, the RPC will shut down, so make sure to put the robot in a **safe position** and connect the **charger** before proceeding.

### Downloads
- updater : [Download](https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/EQrH2XjLvJ9EohytH915Kn0BO4bG8FKaNz1rNG5YD3GcIA?e=aFhdo0)
- You can check the latest RPC updates and release notes at the following link:
[RPC Release Notes on GitHub](https://github.com/RainbowRobotics/rby1-release/releases)

### Usage
  ```bash
  sudo apt-get install -y sshpass
  tar -xvf updater.tar
  cd updater_dist
  chmod +x updater
  ./updater <update file name> <RPC IP address>

  # Example
  ./updater rby1_a_0.3.0.tar.gz 192.168.30.1
  ./updater rby1_a_0.3.0.tar 192.168.30.1
  ```

## How to Extract Logs

The `log_backup` tool allows you to back up RPC logs directly through the UPC. Ensure the UPC is powered on and ready before proceeding.

### Downloads
- log_backup(for UPC) : [Download](https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/ERiwb3eeqsdKmtmBNwQhRL4BiY0Ww_saFcCZfqvs0OpNaQ?e=knc3bm)



### Usage
  ```bash
  sudo apt-get install -y sshpass

  # Make the tool executable
  chmod +x log_backup
  
  # Run the tool
  ./log_backup <RPC IP address>
  
  # Example
  ./log_backup 192.168.30.1
  ```

After running the command, `tar.gz` log file will be generated in the same directory where you executed the program.
Please attach this file when contacting us for analysis, as it will greatly assist in troubleshooting.


## How to Check CAN Communication

The `can_checker` tool allows you to verify whether the CAN communication is functioning correctly. 
> ⚠️ WARNING
> Ensure that the robot’s main power is turned on before proceeding.

### Downloads
- can_checker(for UPC) : [Download](https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/Ec5JW4ye3HRLnkzzDQMc6ZwBAVMw2PLQ_3kE5Olx1vAm3g?e=CbKBz0)

### Usage
```bash
# Make the tool executable
chmod +x can_checker

# Run the tool
./can_checker <RPC IP address>

# Example
./can_checker 192.168.30.1
```

If the communication is functioning correctly, you will see output similar to the following. **The process typically takes around 1-2 minutes to complete.**
```bash
Checking can0 (right_arm)...
[SUCCESS] can0 (right_arm) is communicating!
Checking can1 (left_arm)...
[SUCCESS] can1 (left_arm) is communicating!
Checking can2 (torso)...
[SUCCESS] can2 (torso) is communicating!
Checking can3 (wheel)...
[SUCCESS] can3 (wheel) is communicating!
```
If any issues arise, please save the output and attach it when contacting us for further analysis.


