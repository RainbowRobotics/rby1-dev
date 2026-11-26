# Gripper

These are the specifications for the standard gripper, which is sold as an option. The gripper uses the Dynamixel XM430-W210 actuator.

![rby_gripper_info](/images/options/gripper/rby_gripper_info.png)

The default settings for the Dynamixel are shown in the image below. If these settings are maintained, the 
<a href="https://github.com/RainbowRobotics/rby1-sdk/blob/main/examples/cpp/module_test/gripper.cpp"
   target="_blank" rel="noopener noreferrer">
   examples/cpp/module_test/gripper.cpp
</a>
 code can be used without modification. (The gripper on the right hand is set to ID 0, and the gripper on the left hand is set to ID 1.)

![rby1_gripper_dynamixel_parameters](/images/options/gripper/rby1_gripper_dynamixel_parameters.png)

The gripper is connected to the body’s IO port via the bypass port mounted on the wrist. As shown in the image below, the cable can be connected in a way that allows the use of the RS485 to USB device (U2D2) installed in the PDU. (UPC DP <-> BP0 / UPC DN <-> BP1)

![rby_gripper_io_connection](/images/options/gripper/rby_gripper_io_connection.png)
