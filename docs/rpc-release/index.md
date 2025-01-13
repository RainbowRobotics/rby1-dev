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
- updater(for UPC) : [Download](https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/ETcDpUXsFxNJs69e2TzKxqcBp_kATrQ7jrGgmBQFfQjHOw?e=hRMg1s)
- updater_x86_64 : [Download](https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/EUHYdUtTEMxPpcaxeuc_ycgBt-ko0vaa0Xf7fnUDWNxwHQ?e=8hcp6d)
- You can check the latest RPC updates and release notes at the following link:
[RPC Release Notes on GitHub](https://github.com/RainbowRobotics/rby1-release/releases)

### Usage
  ```bash
  sudo apt-get install -y sshpass

  # Program usage
  chmod +x updater
  ./updater <update file name> <RPC IP address>

  # Example
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