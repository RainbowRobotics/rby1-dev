# RPC Updater

The `updater` tool installs a new software release on the robot PC (RPC).
You run it on the user PC (UPC) or on another Linux PC. It copies the update file to the RPC over SSH, installs it, and reboots the RPC.

::: warning Before you update
- The RPC restarts during the update, and the robot power can turn off. Joints without a brake are then not held.
- Before you start, stop every program that controls the robot. Move the robot to a stable pose (for example the zero pose), disable the Control Manager, and turn the power lines off (see [Shutdown Order](../precautions/power_and_battery.md#shutdown-order)).
- Connect the charger.
- Do not turn off the RPC or disconnect the network until the updater has finished.
:::

## Downloads

- Update files and release notes: <a href="https://github.com/RainbowRobotics/rby1-release/releases" target="_blank" rel="noopener noreferrer">rby1-release on GitHub</a>
- Updater (`updater_dist.tar`): in the Web UI, open **Settings > Utilities** and press **Download Updater**. You can also download it here: <a href="https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/EQrH2XjLvJ9EohytH915Kn0BO4bG8FKaNz1rNG5YD3GcIA?e=aFhdo0" target="_blank" rel="noopener noreferrer">Download</a>

## Choose the update file

Each release has one update file per robot model and hardware version. Use the file that matches your robot.

To check the model and version of your robot, use one of these:

- The bottom of the Web UI **Dashboard** page shows **RPC** (software version), **Model** and **Model Version**.
- The SDK:

  ```python
  import rby1_sdk as rby

  robot = rby.create_robot("192.168.30.1:50051", "a")  # the model argument does not matter for this call
  robot.connect()
  info = robot.get_robot_info()
  print(info.robot_model_name, info.robot_model_version, info.version)
  ```

  `robot_model_name` is the model, `robot_model_version` the hardware version, and `version` the installed robot software version.
  See [Versions of the robot](../getting-started/supported-platforms.md#versions-of-the-robot) for how these versions relate to the SDK version on your PC.

| Robot | Update file |
|---|---|
| Model A, v1.0 / v1.1 / v1.2 | `rby1_a_v1.0-<version>.tar.gz` / `rby1_a_v1.1-<version>.tar.gz` / `rby1_a_v1.2-<version>.tar.gz` |
| Model M, v1.0 / v1.1 / v1.2 / v1.3 | `rby1_m_v1.0-<version>.tar.gz` … `rby1_m_v1.3-<version>.tar.gz` |
| Model UB | `rby1_ub-<version>.tar.gz` |

`<version>` is the release number, for example `0.11.0`.

## Where to run the updater

| Computer | Executable | RPC address | Typical time |
|---|---|---|---|
| UPC (ARM64), wired internal network (recommended) | `updater` | `192.168.30.1` | about 3 minutes |
| Another x86_64 Linux PC on the RPC's Wi-Fi network | `updater_x86_64` | the RPC's Wi-Fi IP | 15–20 minutes or more |
| Another x86_64 Linux PC on the RPC's hotspot | `updater_x86_64` | `192.168.12.1` | 15–20 minutes or more |

The update file is large. Use the UPC and the wired connection when you can.

## Usage

1. Copy the update file and `updater_dist.tar` to the computer that runs the update.
2. Unpack the updater and run it with the update file and the RPC address.

```bash
tar -xvf updater_dist.tar && cd updater_dist

# On the UPC (ARM64)
./updater <update file> <RPC IP address>

# On another x86_64 Linux PC
./updater_x86_64 <update file> <RPC IP address>

# Examples
./updater ~/rby1_m_v1.2-<version>.tar.gz 192.168.30.1
./updater_x86_64 ~/rby1_a_v1.2-<version>.tar.gz 192.168.12.1
```

The updater shows its progress in four steps: it transfers the file, extracts it and runs the install script, updates the scheduled jobs, and reboots the RPC.
When it prints `Update completed successfully.`, wait for the RPC to finish rebooting.

<img :src="$withBase('/images/rpc_management_tools/updater.png')" alt="Terminal output of the updater" class="center white-bg" style="width:100%">

## Check the result

After the RPC has rebooted, check the installed version in one of these places:

- The version at the bottom of the **Dashboard** page in the Web UI.
- The version on the backpack OLED.

<img :src="$withBase('/images/rpc_management_tools/update_result.png')" alt="Software version shown in the Web UI Dashboard and on the backpack OLED" class="center white-bg" style="width:100%">

## If the update fails

- If the updater stops with an `Error:` message before the RPC reboots, check the network connection and the RPC address, then run the updater again with the same file.
- If the install script cannot load the new software, it restores the previous version.
- If the robot does not start after the update, or the updater fails again, back up the logs (see [Log Backup](log_backup.md)), save the terminal output, and contact the support team (<a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>).
