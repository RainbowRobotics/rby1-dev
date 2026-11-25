# Connect to Hotspot & Check Web UI

There are several ways to connect to the robot. The simplest method is to use the **hotspot** function to join the robot’s network and access the Web UI for initial setup.
Through the Web UI, you can also check the robot’s basic status, power it on, and move it into the zero pose

```{warning}
The steps below power the robot, enable its servos and move it to the zero pose.
Read [E‑Stop Basics](estop-basics.md) first, keep the E‑Stop or the remote controller in your hand,
and clear the space around the robot.
```

## Steps
1. Turn on the RPC power.

2. Once the RPC is power on, press the **HOTSPOT** button on top of the backpack.
   - If the button is already active, release it and press again.

3. On your laptop, join the robot’s hotspot SSID (e.g., `RBY1`).  
   - Default password: `RBY1@@@@`.
   :::{admonition} Connecting via QR Code
   :class: note
   1. Press the **HOTSPOT** button on the top of the robot's backpack to activate the hotspot.
   2. A QR code will be displayed; scan it to automatically connect to the network.
   3. The hotspot will remain active only while the **HOTSPOT** button is pressed.
   :::

4. Open the Web UI in a browser: `http://192.168.12.1:5173`. The dashboard shows the robot’s current status (power, joint angles, etc.).

   ```{image} ../_static/images/getting-started/webui_dashboard.png
   :alt: dashboard
   :align: center
   :width: 800px
   :class: white_bg
   ```

5. From the left sidebar, select **Unpacking** to open the setup tab.

   ```{image} ../_static/images/getting-started/webui_sidebar.png
   :alt: sidebar
   :align: center
   :width: 800px
   :class: white_bg
   ```

   - **Step 1.** Turn Power On 
   
      Click the **POWER ON** button to supply power to the robot.

      ```{image} ../_static/images/getting-started/webui_unpacking_step1.png
      :alt: step1
      :align: center
      :width: 800px
      :class: white_bg
      ```

   - **Step 2.** Activate Servo

      Enable the robot’s servos so that joints can move.
      This enables all joints defined in the model.
      If some joints (e.g., the head or mobile base wheels) are removed, enable servos only for the remaining joints in the **Control Panel**.

      ```{image} ../_static/images/getting-started/webui_unpacking_step2.png
      :alt: step2
      :align: center
      :width: 800px
      :class: white_bg
      ```

   - **Step 3.** Enable Control Manager

      Enable the control manager so that the robot can execute controllers.
      If the state shows **Fault**, press **Reset** and try again.

      ```{warning}
      The Unpacking wizard enables the Control Manager only in **Unlimit** mode (**Enable(Unlimit)**).
      Unlimit skips the joint operating range check, so the robot can move outside its joint limits.
      Use it only for unpacking, and switch to the standard mode in Step 5.
      ```

      ```{image} ../_static/images/getting-started/webui_unpacking_step3.png
      :alt: step3
      :align: center
      :width: 800px
      :class: white_bg
      ```

   - **Step 4.** Move to Zero Pose

      Send the robot to the zero pose for initialization.
      The robot moves slowly to a standing position.
      Keep the remote controller in your hand and make sure the path is clear.
      To pause the motion, press **SOFT STOP** at the top of the screen. To cut power immediately, press button 1 on the remote controller.

      ```{image} ../_static/images/getting-started/webui_unpacking_step4.png
      :alt: step4
      :align: center
      :width: 800px
      :class: white_bg
      ```

   - **Step 5.** Switch to the standard mode (required)

      The robot is still in **Unlimit** mode after Step 4.
      Press **Disable**, then press **Enable** on the last page of the wizard to switch the Control Manager to the standard mode,
      in which the joint operating range is checked.
      Do this before you use the SDK, teleoperation or ROS 2.


<!-- ## Notes
- If the Web UI does not load, see **Troubleshooting** section. -->
