# Log Backup

## How to Extract Logs

The `log_backup` tool allows you to back up RPC logs directly through the UPC. Ensure the UPC is powered on and ready before proceeding.

### Downloads (Log Backup)

- log_backup(for UPC) : <a href="https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/ERiwb3eeqsdKmtmBNwQhRL4BiY0Ww_saFcCZfqvs0OpNaQ?e=knc3bm" target="_blank" rel="noopener noreferrer">Download</a>

### Usage (Log Backup)

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
