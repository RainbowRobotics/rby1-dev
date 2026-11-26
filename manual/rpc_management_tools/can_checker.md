# CAN Checker

The `can_checker` tool checks that the robot PC (RPC) receives data on each of its four CAN channels.
You run it on the user PC (UPC) or on another Linux PC that can reach the RPC over SSH. For each channel, it records the CAN traffic on the RPC for 2 seconds. The whole check takes about 10 seconds.

## Download

- can_checker (for the UPC): <a href="https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/IQDOSVuMntx0S55M8w0DHOmcAQFTMNjy0P95BOTpcdbwJt4?e=T0Gu3j" target="_blank" rel="noopener noreferrer">Download</a>

::: warning
Turn on the robot power (48 V) before you run the check. Without it, the motor drivers send no CAN data and their channels are reported as `[FAILURE]`. Follow [Disable the Control Manager Before Changing the Power State](../precautions/power_and_battery.md#disable-the-control-manager-before-changing-the-power-state) when you change the power.
:::

## Usage

```bash
# The tool uses sshpass for the SSH login
sudo apt-get install -y sshpass

# Make the tool executable (once)
chmod +x can_checker

# Run the tool
./can_checker <RPC IP address>

# Example (UPC, wired connection to the RPC)
./can_checker 192.168.30.1
```

If `sshpass` is not installed or the RPC cannot be reached, the tool reports every channel as `[FAILURE]`.

## Results

If all channels communicate, the output looks like this:

```text
Checking can0 (right_arm)...
[SUCCESS] can0 (right_arm) is communicating!
Checking can1 (left_arm)...
[SUCCESS] can1 (left_arm) is communicating!
Checking can2 (torso)...
[SUCCESS] can2 (torso) is communicating!
Checking can3 (wheel)...
[SUCCESS] can3 (wheel) is communicating!
```

The channel labels in the output are short names. For the devices on each channel, see [Communication System Overview \[CAN\]](../hardware/electrical_part.md#communication-system-overview-can).

| Result | Meaning | What to do |
|---|---|---|
| `[SUCCESS] ... is communicating!` | The RPC received data on the channel. | Nothing. |
| `[ERROR] ... has error packets!` | The RPC received data, but some frames look like error frames. | Save the output and back up the logs (see [Log Backup](log_backup.md)). Contact the support team. |
| `[FAILURE] ... has no communication.` | The RPC received no data on the channel. | Check that `sshpass` is installed, that the RPC address is correct, and that the 48 V power is on. Then run the tool again. If the failure stays, save the output and contact the support team. |

Support: <a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>
