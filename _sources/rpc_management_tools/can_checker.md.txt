# CAN Checker

## How to Check CAN Communication

The can_checker tool allows you to verify whether the CAN communication is functioning correctly.

### Downloads (CAN Checker)
- can_checker(for UPC): <a href="https://rainbowco-my.sharepoint.com/:u:/g/personal/rby_support_rainbow-robotics_com/IQDOSVuMntx0S55M8w0DHOmcAQFTMNjy0P95BOTpcdbwJt4?e=T0Gu3j" target="_blank" rel="noopener noreferrer">Download</a>

``` {Warning} Ensure that the robot’s main power is **turned on** before proceeding.
```

### Usage (CAN Checker)
 
```bash
# Make the tool executable
chmod +x can_checker

# Run the tool
./can_checker <RPC IP address>

# Example
./can_checker 192.168.30.1
```

If the communication is functioning correctly, you will see output similar to the following. The process typically takes around 1-2 minutes to complete.

```bash
Checking can0 (right_arm)...
[SUCCESS] can0 (right_arm) is communicating!
Checking can1 (left_arm)...
[SUCCESS] can1 (left_arm) is communicating!
Checking can2 (torso)...
[SUCCESS] can2 (torso) is communicating!
Checking can3 (wheel)...
[SUCCESS] can3 (wheel) is communicating!
```

If any issues arise, please save the output and attach it when contacting us for further analysis.

