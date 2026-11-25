# Initialize the FT Sensor

## How to Initialize the FT Sensor

The `ft_zeroset` tool allows you to check the FT sensor status and perform initialization if supported by the connected sensor firmware.

### Downloads (FT zeroset)
- ft_initialization: <a href="https://rainbowco-my.sharepoint.com/:f:/g/personal/support_rainbow-robotics_com/IgC4sTyb4l6dQppcrBiLWBJtAbmd1wpmB5SQgJTZlQCCKiE?e=bWRSl4">Download</a>

```{Warning}
Ensure that the robot’s main power is **turned on** before proceeding.
```

### Usage (FT zeroset)

```bash
# Install required package
sudo apt-get install sshpass


# For ARM-based systems
chmod +x ./ft_zeroset
./ft_zeroset <RPC_ADDRESS>
## ARM-based systems Example
./ft_zeroset_jetson 192.168.30.1


# For x86_64 systems
chmod +x ./ft_zeroset_x86
./ft_zeroset_x86 <RPC_ADDRESS>
## For x86_64 systems Example
./ft_zeroset_x86 192.168.0.121
```

### Result Guide (FT zerosetn)

#### Success Case (FT zeroset)
```bash
=== Step 0: Power Check ===
[OK] 48V power is already on. It will be left on after exit.

=== Step 1: Firmware Version Check ===

=== Step 2: FT Sensor Bias Initialization ===

=== Result ===
[NEW] right arm (can0): zero set succeeded.
[NEW] left arm (can1): zero set succeeded.

```

#### Failure Cases (FT zeroset)

```bash
=== Step 0: Power Check ===
[OK] 48V power is already on. It will be left on after exit.

=== Step 1: Firmware Version Check ===

=== Result ===
[LEGACY] right arm (can0): zero set not supported version.
[LEGACY] left arm (can1): zero set not supported version.

```

- FAIL → Older version. Bias initialization is not supported.

If FAIL is displayed, please save the terminal output and contact our CS team(<a href="rby.support@rainbow-robotics.com"
   target="_blank" rel="noopener noreferrer">rby.support@rainbow-robotics.com</a>). In this case, an FT sensor firmware update may be required.
