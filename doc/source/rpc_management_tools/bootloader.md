# Bootloader

## How to Run Bootloader

This section describes how to update firmware using the bootloader tool.
Before running the bootloader, make sure the robot is powered on and the correct firmware file is prepared.

### Downloads (Bootloader)
- bootloader: <a href="https://rainbowco-my.sharepoint.com/:f:/g/personal/support_rainbow-robotics_com/IgAPC9hh-MFvS5toN3rIdpiAAUbj6jN0K3uMJGrOATRRq4E?e=bkZcrh">Download</a>

The downloaded files include HEX firmware images for each robot module and bootloader executables for different system architectures.

#### HEX Firmware Files

Each HEX file contains the firmware image for the actuator modules indicated by its file name.

| File name | Target module |
|---|---|
| `com_head_0_1.hex` | head_0, head_1 |
| `com_left_arm_0.hex` | left_arm_0 |
| `com_left_arm_1_2.hex` | left_arm_1,left_arm_2 |
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

#### Bootloader Executables

Select the bootloader executable that matches the architecture of the system where the bootloader will be executed.

| File name | Target system |
|---|---|
| `upc_firmware_bootloader_jetson` | ARM-based systems, such as Jetson |
| `upc_firmware_bootloader_x86` | x86_64 systems |

```{note}
Use the HEX file that matches the target module. Using an incorrect HEX file may erase or flash the wrong actuator.
```

```{Warning}
Ensure that the robot’s main power is **turned off** before proceeding.
```

### Usage (Bootloader)

```bash
## For ARM-based systems
sudo chmod +x upc_firmware_bootloader_jetson
## For x86_64 systems
sudo chmod +x upc_firmware_bootloader_x86


# RUN
./upc_firmware_bootloader_<OS> <RPC IP> <TARGET JOINT> <HEX FILE>
## ex) torso_0.
## For ARM-based systems
./upc_firmware_bootloader_jetson 192.168.30.1 torso_0 com_torso_0_1_2.hex
## For x86_64 systems
./upc_firmware_bootloader_x86 <RPC IP> torso_0 com_torso_0_1_2.hex
```

After running the bootloader command, the flash target confirmation message will be displayed.

```bash
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

If the target joint and HEX file are correct, type yes and press Enter to start the flash process.

```bash
Type "yes" to start flash [yes]: yes
```

### Result Guide (Bootloader)

#### Success Case (Bootloader)

```bash
[DONE] flash sequence complete
```

<br>

#### Failure Cases (Bootloader)

If the bootloader fails, check the error message and rerun the flash process again.
In most cases, the firmware can be recovered by running the bootloader again.

- Unsupported firmware version

This error occurs when the firmware version does not support the bootloader.

```bash
[FAIL] unsupported firmware version for this bootloader
```

<br>

- Incorrect HEX file

This error occurs when the selected .hex file does not match the target joint.

```bash
[ERR] HEX filename <Hex File Name>.hex is not allowed for joint torso_0 (expected=com_torso_0_1_2.hex)
```

Check that the target joint name and .hex filename are correct, then run the bootloader again.

<br>

- Error during Erase

This error occurs when the erase step does not complete normally.

```bash
[STEP] ERASE start (may take up to ~30s)
[WARN] ERASE ack(22) not received, retry 2/2
[SUMMARY] rewrite-required failure: ERASE ack(22) not received after 2 attempts
[RECOVERY] image state is uncertain; rerun the full flash to perform full erase + full rewrite
[STEP] cleanup remote resources
[OK] cleanup done
```

In this case, the firmware image state may be uncertain.
Run the flash process again to perform erase and rewrite.
<br>

- Error during burn

This error occurs when communication fails while writing the firmware.

```bash
[STEP] BURN start (8816/8816 lines)
    progress: 5290/8816 (60%) elapsed=9.99s rate=530 lines/s
[SUMMARY] rewrite-required failure: BL handshake timeout at line 5337 (expected 99)
[RECOVERY] image state is uncertain; rerun the full flash to perform full erase + full rewrite
[STEP] cleanup remote resources
[OK] cleanup done
```

In this case, the firmware write process was interrupted.
Run the flash process again to perform erase and rewrite.

- Unsupported firmware version

This error occurs when the current firmware version is too old to be supported by this bootloader.

```bash
[FAIL] unsupported firmware version for this bootloader
```

If FAIL is displayed, please save the terminal output and contact our CS team(<a href="rby.support@rainbow-robotics.com"
   target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>).