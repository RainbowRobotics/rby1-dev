C++ Examples
============

rby1-sdk |sdk_version| ships its C++ examples in
`examples/cpp <https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/examples/cpp>`__.
The files are numbered. Most numbers match the Python examples in
``examples/python``; ``04`` and ``05`` are swapped.
Each program prints its arguments with ``--help``. Most take
``--address <ip>:50051`` and ``--model a|m``.

To build them, configure the SDK with ``-DBUILD_EXAMPLES=ON`` (see :doc:`build-and-link`).
Each file ``NN_name.cpp`` builds the program ``example_NN_name``.
The programs in ``examples/cpp/dynamics`` build as ``example_dynamics_<name>``.

.. danger::

   Examples marked **Moves the robot** send motion commands. Before you run one,
   check that nobody is near the robot, the area around it is clear, and you can
   reach the E-Stop. See `E-Stop Basics <../../getting-started/estop-basics.md>`_.
   Try a new example in the simulator first when it supports simulation.

.. rubric:: Recommended First Files

- `01_hello_rby1.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/01_hello_rby1.cpp>`__:
  connect and print ``RobotInfo``. The robot does not move.
- `03_robot_state.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/03_robot_state.cpp>`__:
  read one state snapshot. The robot does not move.
- `00_helper.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/00_helper.cpp>`__:
  the ``InitializeRobot()`` (power on, servo on, enable the Control Manager) and
  ``MoveJ()`` helpers that the motion examples include.
- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__:
  the standard command flow with many command types. **Moves the robot.**
- `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__:
  the ``Robot::Control()`` real-time path. **Moves the robot.**

.. rubric:: Connection & State

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `01_hello_rby1.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/01_hello_rby1.cpp>`__
     - :doc:`client/robot`, :doc:`state/robot-info`
     - Connect and print the robot information.
   * - `02_robot_model_setting.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/02_robot_model_setting.cpp>`__
     - ``GetRobotModel()``, ``ImportRobotModel()``
     - Read the robot model (URDF), save a custom model, and select it. The
       selection applies after a reboot.
   * - `03_robot_state.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/03_robot_state.cpp>`__
     - :doc:`state/robot-state`
     - Power on the selected devices and print one state snapshot.
   * - `04_parameter.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/04_parameter.cpp>`__
     - ``GetParameter()``, ``SetParameter()``
     - List, read, and set robot parameters.
   * - `05_robot_state_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/05_robot_state_stream.cpp>`__
     - ``StartStateUpdate()``
     - Receive state updates in a callback.
   * - `06_state_tool_flange.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/06_state_tool_flange.cpp>`__
     - :doc:`state/robot-state`
     - Power on the tool flange supply and print the tool flange states.
   * - `07_power.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/07_power.cpp>`__
     - ``PowerOn()``, ``PowerOff()``
     - Turn device power on.
   * - `08_check_firmware_version.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/08_check_firmware_version.cpp>`__
     - :doc:`state/robot-info`
     - Print motor name, brake, product name, and firmware version.

.. rubric:: Settings & System

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `09_get_pid_gain.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/09_get_pid_gain.cpp>`__
     - ``Get*PositionPIDGains()``
     - Read the position PID gains. Does not run in simulation.
   * - `10_set_pid_gain.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/10_set_pid_gain.cpp>`__
     - ``SetPositionPIDGain()``
     - Change position PID gains. The factory gains are tuned; wrong gains can
       cause accidents. Does not run in simulation or while the Control Manager
       is enabled.
   * - `11_factory_default_pid_gain.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/11_factory_default_pid_gain.cpp>`__
     - ``SetPositionPIDGain()``
     - Write factory default PID gains. The example itself recommends not to
       use it. Does not run in simulation.
   * - `12_led.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/12_led.cpp>`__
     - ``SetLEDColor()``
     - Control the LED.
   * - `13_set_system_time.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/13_set_system_time.cpp>`__
     - ``GetSystemTime()``, ``SetSystemTime()``
     - Read and set the robot PC (RPC) system time and time zone. Not supported
       in simulation.
   * - `14_wifi.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/14_wifi.cpp>`__
     - ``ScanWifi()``, ``ConnectWifi()``
     - Set up the robot Wi-Fi connection. The change can take 1 to 2 minutes.
       Does not run in simulation.

.. rubric:: Logs

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `15_log.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/15_log.cpp>`__
     - ``GetLastLog()``, :doc:`state/log`
     - Print the most recent log entries.
   * - `16_log_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/16_log_stream.cpp>`__
     - ``StartLogStream()``
     - Receive log entries in a callback.
   * - `17_fault_log.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/17_fault_log.cpp>`__
     - ``GetFaultLogList()``, ``DownloadFile()``
     - List fault log files and download the first one as ``fault.csv``.

.. rubric:: Dynamics

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `18_dynamics_modeling.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/18_dynamics_modeling.cpp>`__
     - :doc:`models/dyn-link`, :doc:`models/dyn-joint`
     - Build a two-link model in code and compute forward kinematics. No robot
       needed.
   * - `19_dynamics_robot.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/19_dynamics_robot.cpp>`__
     - ``GetDynamics()``, :doc:`models/dyn-robot`
     - Get the robot dynamics model and compute inverse dynamics.
   * - `dynamics/ <https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/examples/cpp/dynamics>`__
     - :doc:`models/dyn-robot`, :doc:`models/dyn-state`
     - ``load_urdf``, ``mass_matrix``, ``inverse_dynamics``, ``gravity_term``,
       ``dynamics_coeff``, ``reflective_mass``, ``simple_robot``: dynamics
       computations on a URDF or an in-code model. No robot needed.

.. rubric:: Motion & Commands

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `21_record.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/21_record.cpp>`__
     - ``StartStateUpdate()``
     - Record joint positions to a file. The robot does not move.
   * - `22_replay.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/22_replay.cpp>`__
     - :doc:`client/robot-command-stream-handler`
     - Replay recorded positions. **Moves the robot.**
   * - `23_zero_pose.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/23_zero_pose.cpp>`__
     - :doc:`builders/joint-position-command-builder`
     - Move the body to the zero pose. **Moves the robot.**
   * - `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__
     - :doc:`builders/robot-command-builder` and most builders
     - Joint position, Cartesian, impedance, optimal control, gravity
       compensation, and mixed commands in sequence. **Moves the robot**
       with large motions.
   * - `25_wiggle_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/25_wiggle_motion.cpp>`__
     - :doc:`builders/joint-impedance-control-command-builder`
     - Circular torso motion with joint impedance control. **Moves the robot.**
   * - `26_cancel_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/26_cancel_control.cpp>`__
     - ``CancelControl()``
     - Start a motion and cancel it. **Moves the robot.**
   * - `27_collisions.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/27_collisions.cpp>`__
     - ``CancelControl()``, :doc:`state/robot-state`
     - Watch the collision distance during a motion and stop when it gets too
       small. **Moves the robot.**
   * - `28_cartesian_impedance_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/28_cartesian_impedance_control.cpp>`__
     - :doc:`builders/impedance-control-command-builder`, :doc:`builders/cartesian-command-builder`
     - Cartesian command, then impedance control of the right arm.
       **Moves the robot.**
   * - `29_joint_impedance_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/29_joint_impedance_control.cpp>`__
     - :doc:`builders/joint-impedance-control-command-builder`
     - Joint impedance control of both arms. **Moves the robot.**
   * - `30_joint_group_command.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/30_joint_group_command.cpp>`__
     - :doc:`builders/joint-group-position-command-builder`
     - Joint group command. Available only on the torso. Does not run in
       simulation. **Moves the robot.**
   * - `31_multi_controls.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/31_multi_controls.cpp>`__
     - ``SendCommand(builder, priority)``
     - Overlapping body and arm commands with different priorities; prints the
       finish code of each. **Moves the robot.**
   * - `32_command_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/32_command_stream.cpp>`__
     - :doc:`client/robot-command-stream-handler`
     - Stream joint position commands in a loop. **Moves the robot.**
   * - `33_cartesian_command_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/33_cartesian_command_stream.cpp>`__
     - :doc:`client/robot-command-stream-handler`, :doc:`builders/cartesian-command-builder`
     - Stream right-arm Cartesian targets and read feedback. **Moves the robot.**
   * - `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__
     - ``Control()``, :doc:`client/control-loop-types`, :doc:`models/trapezoidal-motion-generator`
     - Real-time control loop with your own controller. **Moves the robot.**
   * - `37_mobile_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/37_mobile_test.cpp>`__
     - :doc:`builders/se2-velocity-command-builder`
     - Drive the mobile base with SE(2) velocity commands. **Moves the robot**
       across the floor; clear the floor area first.

.. rubric:: Leader Arm, Brakes & Peripherals

.. list-table::
   :header-rows: 1
   :widths: 30 26 44

   * - Example
     - Main API
     - What it does
   * - `20_leader_arm_state_check.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/20_leader_arm_state_check.cpp>`__
     - :doc:`utilities/leader-arm`
     - Initialize the leader arm on the user PC (UPC) and print its state in a
       gravity-compensated current-control loop. Not supported in simulation.
   * - `35_leader_arm_teleop_with_monitor.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/35_leader_arm_teleop_with_monitor.cpp>`__
     - :doc:`utilities/leader-arm`, :doc:`client/robot-command-stream-handler`
     - Teleoperation: the robot arms and grippers follow the leader arm.
       Not supported in simulation. **Moves the robot.**
   * - `36_brake_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/36_brake_test.cpp>`__
     - ``BrakeRelease()``, ``BrakeEngage()``
     - Release and engage the brake of one joint. The joint can move under
       gravity. The example refuses torso joints and ``.*``.
   * - `38_serial_device.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/38_serial_device.cpp>`__
     - ``GetSerialDeviceList()``
     - List serial devices on the robot. Does not run in simulation.
   * - `39_serial_communication.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/39_serial_communication.cpp>`__
     - :doc:`client/serial-stream`
     - Open a serial stream, read with a callback, and write data. Does not run
       in simulation.

Verified against: rby1-sdk v0.10.1 ``examples/cpp/*.cpp`` (file headers and API calls),
``examples/cpp/CMakeLists.txt``, ``examples/cpp/dynamics/CMakeLists.txt``.
