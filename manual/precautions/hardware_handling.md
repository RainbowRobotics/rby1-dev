# Hardware Handling

## Connecting and Disconnecting the MOCO Cable

::: info NOTICE
The MOCO cable connects the leader arm to the RB-Y1 backpack. Inserting the connector at the wrong angle, or pulling on the cable, can damage the connector and the cable.

- Align the red dot on the cable connector with the red mark on the port before you insert it.
- To disconnect, hold the connector housing. Do not pull on the cable.
:::

Both the RB-Y1 backpack (**U-PC M/ARM** port) and the leader arm have a MOCO cable port.

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/master_arm.png')" alt="MOCO cable port on the leader arm" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/backpack.png')" alt="MOCO cable port labeled U-PC M/ARM on the RB-Y1 backpack panel" class="white-bg">

</div>

</div>

When you connect the MOCO cable to the RB-Y1 backpack or the leader arm, align the red dot on the cable housing with the red square on the port, then insert it.

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/backpack_moco1.jpg')" alt="MOCO connector at the backpack port, red dot and red mark" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/backpack_moco2.jpg')" alt="MOCO connector on the backpack port with the red dot lined up with the red square" class="white-bg">

</div>

</div>

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/masterarm_moco4.jpg')" alt="MOCO connector at the leader arm port, red dot and red mark" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/masterarm_moco3.jpg')" alt="MOCO connector on the leader arm port with the red dot lined up with the red mark" class="white-bg">

</div>

</div>

When you disconnect the MOCO cable, do not pull on the cable itself.

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/backpack_moco3.png')" alt="Wrong: pulling the MOCO cable out of the backpack port by the cable" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/masterarm_moco1.png')" alt="Wrong: pulling the MOCO cable out of the leader arm port by the cable" class="white-bg">

</div>

</div>

Always hold the connector housing when you remove the cable.

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/backpack_moco4.jpg')" alt="Right: holding the connector housing to remove the MOCO cable from the backpack" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/masterarm_moco2.jpg')" alt="Right: holding the connector housing to remove the MOCO cable from the leader arm" class="white-bg">

</div>

</div>

---
## Tool Flange Connector

::: info NOTICE
Forcing the tool flange connector in at the wrong angle can damage it.

- Align the connector with the keyway (groove) before you insert it.
- Do not force the connection.
:::

<div class="media-grid" style="--cols:2">

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/tf_connect1.jpg')" alt="Tool flange cable connector face with its keyway notch" class="white-bg">

</div>

<div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/tf_connect2.jpg')" alt="Tool flange connector keyway, second view" class="white-bg">

</div>

</div>

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/tf_connect3.png')" alt="Tool flange connector on the wrist before (left) and after (right) the cable is connected" class="white-bg" style="width:100%">

---
## Tool Flange Voltage for the Gripper (12V)

::: info NOTICE
The standard RB gripper runs on **12V**. If the tool flange outputs 24V while the standard gripper is connected, the gripper can be permanently damaged.

- Set the tool flange output to 12V before you use the standard gripper.
- Check the output voltage after each power-on, before you connect or use the gripper.
:::

The tool flange output can be off, 12V or 24V. It can be set only while the 48V power is on. Set it in one of these ways:

- **Web UI:** in the **Control Panel**, open the **Tool Flange Power** card. Select **Right** and/or **Left**, select **12V**, and press **ON**. The chips above the buttons show the current output voltage of each arm (for example `Right: 12V`). In older Web UI versions, the card has a **12V ON** button instead (shown below).
- **Python SDK:** `robot.set_tool_flange_output_voltage("right", 12)` (use `"left"` for the left arm, `0` turns the output off). It returns `False` if the command fails. Read the current value from the robot state: `state.tool_flange_right.output_voltage`.
- **ROS 2:** the `tool_flange_power` service (see [Services](../ros2/ros2_driver/services.md)).

<img :src="$withBase('/images/safety_and_precautions/hardware_handling/toolflange_power.png')" alt="Tool Flange Power card in an older Web UI with the 24V ON, 12V ON and OFF buttons; 12V ON is highlighted" class="white-bg" style="width:100%">

See also [Gripper](../options/gripper.md).
