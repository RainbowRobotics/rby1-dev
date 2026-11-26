# Bootloader

The bootloader tool writes new firmware to the motor drivers of RB-Y1 over CAN.
You run it on the user PC (UPC) or on another Linux PC. It connects to the robot PC (RPC) over SSH and sends the CAN commands from there.

::: danger Before you flash firmware
- The robot PC (RPC) must be **on** and reachable over the network. The tool connects to it over SSH.
- The tool switches the motor power by itself during the flash. Before you start, stop every program that controls the robot, put the robot in a stable pose with the arms resting or supported, disable the Control Manager, and then turn the servos and the motor power (48 V) **off** (see [Disable the Control Manager Before Changing the Power State](../precautions/power_and_battery.md#disable-the-control-manager-before-changing-the-power-state)).
- Keep the charger connected or make sure the battery is charged.
- Do not turn off the RPC or disconnect the network while the tool erases or writes the firmware. Press the E-Stop only in an emergency. If the flash is interrupted, run it again (see [Failure cases](#failure-cases)).
- Flash only the joint that you need to update, with the HEX file listed for it below.
:::

## Downloads

- Bootloader package: <a href="https://rainbowco-my.sharepoint.com/:f:/g/personal/support_rainbow-robotics_com/IgAPC9hh-MFvS5toN3rIdpiAAUbj6jN0K3uMJGrOATRRq4E?e=bkZcrh" target="_blank" rel="noopener noreferrer">Download</a>

The package contains HEX firmware images for the motor drivers and the bootloader executables.

### HEX firmware files

Each HEX file is the firmware image for the joints in its file name.

| File name | Target joints |
|---|---|
| `com_head_0_1.hex` | head_0, head_1 (v1.2 and v1.3 only; see the note below) |
| `com_left_arm_0.hex` | left_arm_0 |
| `com_left_arm_1_2.hex` | left_arm_1, left_arm_2 |
| `com_left_arm_3.hex` | left_arm_3 |
| `com_left_arm_4.hex` | left_arm_4 |
| `com_left_arm_5.hex` | left_arm_5 |
| `com_right_arm_0_1_2.hex` | right_arm_0, right_arm_1, right_arm_2 |
| `com_right_arm_3.hex` | right_arm_3 |
| `com_right_arm_4.hex` | right_arm_4 |
| `com_right_arm_5.hex` | right_arm_5 |
| `com_torso_0_1_2.hex` | torso_0, torso_1, torso_2 |
| `com_torso_3_5.hex` | torso_3, torso_5 |
| `com_torso_4.hex` | torso_4 |

- The package has no HEX file for right_arm_6, left_arm_6 or the wheels. Contact support if one of these joints needs a firmware update.
- On v1.0 and v1.1 robots, head_0 and head_1 are Dynamixel actuators, not CAN motor drivers. Do not use `com_head_0_1.hex` on these robots.
- The table lists the joint names of Model A and Model M. Contact support before you flash a Model UB robot.

::: warning
Use the HEX file that matches the target joint. A wrong HEX file can erase or flash the wrong actuator.
:::

### Bootloader executables

Use the executable that matches the CPU of the computer that runs the tool.

| File name | Computer |
|---|---|
| `upc_firmware_bootloader_jetson` | ARM64, for example the UPC (Jetson) |
| `upc_firmware_bootloader_x86` | x86_64 Linux PC |

## Usage

```bash
# Make the executable runnable (once)
chmod +x upc_firmware_bootloader_jetson   # ARM64 (UPC)
chmod +x upc_firmware_bootloader_x86      # x86_64

# Run
./upc_firmware_bootloader_<ARCH> <RPC IP> <TARGET JOINT> <HEX FILE>

# Example: flash torso_0 from the UPC (wired connection to the RPC)
./upc_firmware_bootloader_jetson 192.168.30.1 torso_0 com_torso_0_1_2.hex

# Example: flash torso_0 from an x86_64 PC on the RPC's Wi-Fi network
./upc_firmware_bootloader_x86 <RPC Wi-Fi IP> torso_0 com_torso_0_1_2.hex
```

`<ARCH>` is `jetson` or `x86`. `<TARGET JOINT>` is one joint name, for example `torso_0`.

The tool flashes one joint per run. When one HEX file covers several joints (for example `com_torso_0_1_2.hex`), run the tool once for each joint that you update.

After you start the command, the tool shows the flash target and asks for confirmation.
It has not sent any SSH, power, erase or write command at this point.

```text
========================================
 UPC->RPC CAN Bootloader Flash (native RPC burn worker)
========================================
[OK] HEX parsed
========================================
 FLASH TARGET CONFIRMATION
========================================
[TARGET] joint=torso_0
[TARGET] hex=com_torso_0_1_2.hex
[WARN] Wrong CAN/BNO/HEX can erase or flash the wrong actuator.
[WARN] No SSH, power, erase, or burn command has been sent yet.
Type "yes" to start flash [yes]:
```

Check the joint and the HEX file. If both are correct, type `yes` and press Enter to start the flash.

```text
Type "yes" to start flash [yes]: yes
```

## Results

### Success

```text
[DONE] flash sequence complete
```

### Failure cases

If the flash fails, read the error message and run the tool again.
In most cases, running the full flash again recovers the firmware.

**Unsupported firmware version**

The firmware on the driver is too old for this bootloader.

```text
[FAIL] unsupported firmware version for this bootloader
```

Do not retry. Save the terminal output and contact the support team (<a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>).

**Wrong HEX file**

The HEX file does not match the target joint.

```text
[ERR] HEX filename <Hex File Name>.hex is not allowed for joint torso_0 (expected=com_torso_0_1_2.hex)
```

Check the joint name and the HEX file name, then run the tool again.

**Error during erase**

The erase step did not finish.

```text
[STEP] ERASE start (may take up to ~30s)
[WARN] ERASE ack(22) not received, retry 2/2
[SUMMARY] rewrite-required failure: ERASE ack(22) not received after 2 attempts
[RECOVERY] image state is uncertain; rerun the full flash to perform full erase + full rewrite
[STEP] cleanup remote resources
[OK] cleanup done
```

The firmware image may be incomplete. Run the full flash again; it erases and rewrites the image.

**Error during write (burn)**

Communication failed while the firmware was written.

```text
[STEP] BURN start (8816/8816 lines)
    progress: 5290/8816 (60%) elapsed=9.99s rate=530 lines/s
[SUMMARY] rewrite-required failure: BL handshake timeout at line 5337 (expected 99)
[RECOVERY] image state is uncertain; rerun the full flash to perform full erase + full rewrite
[STEP] cleanup remote resources
[OK] cleanup done
```

The write was interrupted. Run the full flash again; it erases and rewrites the image.

If the flash still fails after you run it again, save the terminal output and contact the support team.
