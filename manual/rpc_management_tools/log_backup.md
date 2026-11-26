# Log Backup

The robot PC (RPC) keeps its logs in `/root/.rby1/logs`. Attach these logs when you report a problem to the support team (see [Error Reporting](../sdk/troubleshooting/error_reporting.md)).

## Download logs from the Web UI (recommended)

1. Open the Web UI and go to **Settings > Utilities**.
2. Under **Log Downloads**, press one of the buttons:
   - **Download Recent Logs**: only the newest 10 logs. The file is much smaller.
   - **Download All Logs**: every log on the RPC.

The download starts in a new browser tab. Only one log download can run at a time. If another download is running, wait until it has finished and try again.

## Copy logs with the log_backup tool

Use the `log_backup` tool when the Web UI is not available. You run it on the user PC (UPC) or on another Linux PC that can reach the RPC over SSH.

### Download

- log_backup (for the UPC): <a href="https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/ERiwb3eeqsdKmtmBNwQhRL4BiY0Ww_saFcCZfqvs0OpNaQ?e=knc3bm" target="_blank" rel="noopener noreferrer">Download</a>

### Usage

::: tip Accept the RPC host key first
The tool logs in with `ssh` but cannot answer the host key question. On a PC that has never connected to this RPC, the login fails. Connect once by hand before you run the tool:

```bash
ssh root@<RPC IP address>
# Answer "yes" to the host key question. Then press Ctrl+C at the password prompt.
```

If `ssh` reports `REMOTE HOST IDENTIFICATION HAS CHANGED` (for example after the RPC software was reinstalled), remove the old key with `ssh-keygen -R <RPC IP address>` and connect once again.
The source code and the released binary were not compared, so this step is based on the source code.
:::

```bash
# The tool uses sshpass for the SSH login
sudo apt-get install -y sshpass

# Make the tool executable (once)
chmod +x log_backup

# Run the tool
./log_backup <RPC IP address>

# Example (UPC, wired connection to the RPC)
./log_backup 192.168.30.1
```

The tool compresses the log folder on the RPC and copies it to `logs.tar.gz` in the current directory.

::: warning
The tool always writes to `logs.tar.gz` and overwrites an existing file with that name. Rename or move an earlier backup before you run the tool again.
:::

If the tool prints `Error compressing logs.` or `Error downloading logs.`, check that `sshpass` is installed, that the RPC address is correct, that the RPC host key was accepted (see [Usage](#usage)), and that the RPC is reachable (for example with `ping`).
