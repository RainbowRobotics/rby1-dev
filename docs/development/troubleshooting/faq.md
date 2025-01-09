---
title: FAQ
outline: deep 
---

# FAQ

### Q: When I press the enable button in the control, nothing happens, and the control mode remains in the `idle` state. What could be the cause, and how can I resolve it?

**A:**  
This issue may occur when the robot is near a joint limit. If a `servo on` operation is performed when a joint is beyond its limit, the control manager state cannot be switched to `enabled`.  
To resolve this:  
- Set the joints slightly away from the limit using the physical brake release button while the power is off.  
- Once this adjustment is made, try the process again.  
- Additionally, open two log windows during this process to help identify which joint is causing the limit issue.  

> :bulb: Make sure you are connected to the dashboard. The logs will only be recorded when the dashboard is accessed, so ensure you are logged in to view the relevant information.


---

### Q: How can I integrate arm commands with wheel navigation?

**A:**  
When the robot is navigating with a controller, other controllers cannot interfere. To perform arm commands simultaneously, it is recommended to use the `whole_body_command`. This allows you to send arm joint commands within the same stream command, enabling both arm and navigation control to work together.

---

### Q: What happens when I send a set command to only some joints, while the rest of the joints continue moving?

**A:**  
If you send a new command to some joints while another command is already being executed, the new command will be handled according to its priority. There is no simultaneous execution of previous and new commands. If the new command has higher priority, the current position will be locked, and the controller will switch to the new command. If the priority is lower, the command will be refused.

Priority works on a scale from 0 to 100, where a higher number indicates higher priority. For example, if a command with priority 10 is running and a new command with priority 20 comes in, the previous command will stop, and the new one will start, triggering a controller switch.

---

### Q: What is the difference between `stream` and `send_once`?

**A:**  
The difference between `stream` and `send_once` is that `stream` is used for continuous data transmission, suitable when real-time trajectory input or ongoing feedback is required. It continuously sends commands or data.  
In contrast, `send_once` is used to send a single command just once, typically for actions such as moving to a specific waypoint or sending a one-time instruction.


### Q: What is the meaning of `send_command().get()`?

**A:**  
`send_command().get()` is used to send a command and wait until it is fully executed before returning. The `get()` function blocks the execution, ensuring that the command has been completed before proceeding with the next operation.

---

### Q: What happens when a stream is canceled?

**A:**  
When a stream is canceled, the controller switch occurs, and the last encoder position is locked as the reference.

---

### Q: How can I receive sensor feedback while in a stream?

**A:**  
To receive sensor feedback in one request, you can use the `get_state()` function. However, if you need to continuously receive robot status, it is recommended to use `start_state_update` to receive data through the stream channel. This is similar to the command transmission method, where there are both once and stream channels for status reception.

For examples, you can refer to `examples/python/03_robot_state.py` and `examples/python/04_robot_state_stream.py`.

In summary:
- **Send Once**: A one-time request-response structure similar to HTTP, where the client sends a request, and the server responds once.
- **Stream**: Allows continuous data transfer between the client and server, providing real-time updates.

---

### Q: The `teleoperation_with_joint_mapping` example is not running. What could be the cause, and how can I resolve it?

**A:**  
There are several potential reasons for this issue. Please check the following:  
- Ensure the master arm and the UPC master arm are properly connected via cable.  
- Ensure the bypass port of the UPC has a jumper installed.  
- Make sure you grant `sudo` permissions when running the program, as it requires USB device access.

If you don't want to use `sudo` every time you execute the command, follow the steps below:

> :collision: **Warning:** Modifying the udev rules for `u2d2` is entirely at the user's own risk. Any issues resulting from changes to these settings, including losing the serial number, will be considered user fault. Please ensure that you back up the original settings before making any modifications. If issues arise and the serial number is lost, it will be treated as customer negligence. Proceed with caution.

1. **Backup the existing udev rules file**:  
   Before making any changes, it’s a good idea to back up the current configuration.
   ```bash
   sudo cp /etc/udev/rules.d/99-u2d2.rules /etc/udev/rules.d/99-u2d2.rules.bak
   ```

2. **Open the udev rules file**:
   ```bash
   sudo gedit /etc/udev/rules.d/99-u2d2.rules
   ```

3. **The default setting should look like this**:
   ```bash
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_gripper" 
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_master_arm"
   ```

4. **Modify it to the following to allow broader permissions**:
   ```bash
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_gripper", MODE="0666", RUN+="/bin/chmod 666 /sys/bus/usb-serial/devices/%k/latency_timer" 
   SUBSYSTEM=="tty", ATTRS{serial}=="your_serial_number", SYMLINK+="rby1_master_arm", MODE="0666", RUN+="/bin/chmod 666 /sys/bus/usb-serial/devices/%k/latency_timer"
   ```

5. **Reload the udev rules**:
   ```bash
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

6. **Check if the devices are listed correctly by running**:
   ```bash
   ls /dev/rb*
   ```
   You should see `rby1_gripper` and `rby1_master_arm` listed.

7. **If the devices do not show up correctly, you can restore the backup**:
   If `ls /dev/rb*` does not show the expected devices, you can restore the original udev rules by running:
   ```bash
   sudo cp /etc/udev/rules.d/99-u2d2.rules.bak /etc/udev/rules.d/99-u2d2.rules
   sudo udevadm control --reload-rules
   sudo udevadm trigger
   ```

---
### Q: How can I disassemble the robot arm?

**A:**  
Please refer to the attached GIF for an easy step-by-step guide.
1.	Ensure the robot is powered off before proceeding.
2.	Remove the 4 bolts and detach the rear cover.
3.	Disassemble the robot arm and prepare it for your next task.


<figure>
    <img src="/images/arm_disassembly.gif" alt="Arm Disassembly Guide" />
</figure>


---