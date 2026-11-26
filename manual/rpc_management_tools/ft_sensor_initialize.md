# FT Sensor Initialization

The `ft_zeroset` tool checks the force/torque (F/T) sensors in both wrists and sets their zero (bias) if the sensor firmware supports it.
You run it on the user PC (UPC) or on another Linux PC that can reach the robot PC (RPC) over SSH.

::: info Applies to
Robots with wrist F/T sensors. The robot core reads a right (`can0`) and a left (`can1`) F/T sensor on Model A, Model M and Model UB.
The original hardware version table lists no F/T sensor for Model M v1.3. If a sensor is not fitted or does not answer, the tool reports `[FAILURE] ...: hardware detection failed.` for that side.
To check the model and version of your robot, see [Hardware Versions](../sdk/models/hardware-versions.md).
:::

## What the tool does

1. It checks the 48 V power and the E-Stop state.
   - If the E-Stop is pressed, it stops and sends no power command.
   - If the 48 V power is off, the tool turns it on, and turns it off again after it reports the result.
   - If the 48 V power is already on, the tool leaves it on.
2. It reads the firmware version of the right (`can0`) and left (`can1`) F/T sensors.
3. On sensors with a supported firmware, it sets the current reading as zero.

::: warning Before you run the tool
- The zero set takes the current sensor reading as zero. Remove every external load and contact from both hands and grippers before you run it. Do not touch the arms while it runs.
- The tool can turn on the 48 V power. Stop every program that controls the robot and keep people away from the robot.
- Release the E-Stop. The tool does not run while the E-Stop is pressed.
:::

## Download

- ft_zeroset package: <a href="https://rainbowco-my.sharepoint.com/:f:/g/personal/support_rainbow-robotics_com/IgC4sTyb4l6dQppcrBiLWBJtAbmd1wpmB5SQgJTZlQCCKiE?e=bWRSl4" target="_blank" rel="noopener noreferrer">Download</a>

The package has one executable for each CPU type:

| File name | Computer |
|---|---|
| `ft_zeroset_jetson` | ARM64, for example the UPC (Jetson) |
| `ft_zeroset_x86` | x86_64 Linux PC |

## Usage

```bash
# The tool uses sshpass for the SSH login
sudo apt-get install -y sshpass

# On the UPC (ARM64)
chmod +x ./ft_zeroset_jetson
./ft_zeroset_jetson <RPC IP address>
# Example (wired connection to the RPC)
./ft_zeroset_jetson 192.168.30.1

# On another x86_64 Linux PC
chmod +x ./ft_zeroset_x86
./ft_zeroset_x86 <RPC IP address>
# Example (PC on the RPC's Wi-Fi network)
./ft_zeroset_x86 <RPC Wi-Fi IP>
```

## Results

### Success

```text
=== Step 0: Power Check ===
[OK] 48V power is already on. It will be left on after exit.

=== Step 1: Firmware Version Check ===

=== Step 2: FT Sensor Bias Initialization ===

=== Result ===
[NEW] right arm (can0): zero set succeeded.
[NEW] left arm (can1): zero set succeeded.
```

### Firmware does not support zero set

```text
=== Step 0: Power Check ===
[OK] 48V power is already on. It will be left on after exit.

=== Step 1: Firmware Version Check ===

=== Result ===
[LEGACY] right arm (can0): zero set not supported version.
[LEGACY] left arm (can1): zero set not supported version.
```

`[LEGACY]` means that the sensor firmware is older and does not support the zero set. The sensor may need a firmware update. Save the terminal output and contact the support team (<a href="mailto:rby.support@rainbow-robotics.com" target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>).

### Other messages

| Message | Meaning | What to do |
|---|---|---|
| `[NEW] ...: zero set failed.` | The sensor supports the zero set, but the command failed. | Run the tool again. If it fails again, contact the support team. |
| `[FAILURE] ...: hardware detection failed.` | The sensor did not answer the version query. | Check that the 48 V power is on and run the tool again. If it fails again, contact the support team. |
| `[FATAL] EMO switch is pressed. ...` | The E-Stop is pressed. | Release the E-Stop and run the tool again. |
| `[FATAL] SSH authentication failed ...` or `[FATAL] SSH connection failed ...` | The tool cannot log in to the RPC. | Check the RPC address and the network, and check that `sshpass` is installed. |
| `[FATAL] failed to determine initial 48V power state ...` | The tool could not read the power state, so it does not change the power. | Run the tool again. If it fails again, contact the support team. |
