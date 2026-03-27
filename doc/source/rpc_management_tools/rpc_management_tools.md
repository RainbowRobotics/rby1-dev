# RPC Management Tools

## How to Update RPC

Please use the provided `updater` program to update your RPC. During the update, the RPC will shut down, so make sure to put the robot in a safe position and connect the charger before proceeding.

### Downloads
- updater : <a href="https://rainbowco-my.sharepoint.com/personal/rby_support_rainbow-robotics_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Frby%5Fsupport%5Frainbow%2Drobotics%5Fcom%2FDocuments%2Frpc%5Ftools%2Fupdater%5Fdist%2Etar&parent=%2Fpersonal%2Frby%5Fsupport%5Frainbow%2Drobotics%5Fcom%2FDocuments%2Frpc%5Ftools&ga=1" target="_blank" rel="noopener noreferrer">Download</a>
- You can check the latest RPC updates and release notes at the following link: <a href="https://github.com/RainbowRobotics/rby1-release/releases" target="_blank" rel="noopener noreferrer">RPC Release Notes on GitHub</a>

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

---
## How to Extract Logs

The `log_backup` tool allows you to back up RPC logs directly through the UPC. Ensure the UPC is powered on and ready before proceeding.

### Downloads

- log_backup(for UPC) : <a href="https://rainbowco-my.sharepoint.com/personal/rby_support_rainbow-robotics_com/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Frby%5Fsupport%5Frainbow%2Drobotics%5Fcom%2FDocuments%2Frpc%5Ftools%2Flog%5Fbackup&parent=%2Fpersonal%2Frby%5Fsupport%5Frainbow%2Drobotics%5Fcom%2FDocuments%2Frpc%5Ftools&ga=1" target="_blank" rel="noopener noreferrer">Download</a>

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

After running the command, `tar.gz` log file will be generated in the same directory where you executed the program. Please attach this file when contacting us for analysis, as it will greatly assist in troubleshooting.