.. _python_api:

Python API Reference
====================

.. currentmodule:: rby1_sdk

This reference is generated from **rby1-sdk** |sdk_version|. Names that
changed in v0.10.0 are listed under their current names: ``break_engage`` /
``break_release`` became ``brake_engage`` / ``brake_release``, and
``upc.MasterArm`` became ``upc.LeaderArm``.

.. rubric:: Install

Install the version this reference documents:

.. code-block:: bash

   pip install rby1-sdk==0.10.1

For the full setup and a first state check with the robot, see
`SDK Installation and Read State <../../getting-started/sdk-install-and-state.md>`_.
Runnable programs are in
`examples/python <https://github.com/RainbowRobotics/rby1-sdk/tree/v0.10.1/examples/python>`__
of rby1-sdk v0.10.1.

.. rubric:: Typical Flow

The motion examples follow these steps (``initialize_robot()`` and ``movej()``
in ``examples/python/00_helper.py``): create the robot object for your model,
connect, power on, servo on, reset a Control Manager fault if there is one,
enable the Control Manager, send a command, and wait for its feedback.

.. code-block:: python

   import numpy as np
   import rby1_sdk as rby

   robot = rby.create_robot("192.168.30.1:50051", "a")  # model "a", "m" or "ub"
   if not robot.connect():
       raise SystemExit("connect failed")

   # ".*" is a regex that matches every device.
   if not robot.is_power_on(".*") and not robot.power_on(".*"):
       raise SystemExit("power on failed")
   if not robot.is_servo_on(".*") and not robot.servo_on(".*"):
       raise SystemExit("servo on failed")
   if robot.get_control_manager_state().state in (
       rby.ControlManagerState.State.MajorFault,
       rby.ControlManagerState.State.MinorFault,
   ):
       robot.reset_fault_control_manager()
   if not robot.enable_control_manager():
       raise SystemExit("enable control manager failed")

   # Move the torso and both arms to the zero pose in at least 5 s. This moves the robot.
   model = robot.model()
   body = (
       rby.BodyComponentBasedCommandBuilder()
       .set_torso_command(rby.JointPositionCommandBuilder()
                          .set_minimum_time(5).set_position(np.zeros(len(model.torso_idx))))
       .set_right_arm_command(rby.JointPositionCommandBuilder()
                              .set_minimum_time(5).set_position(np.zeros(len(model.right_arm_idx))))
       .set_left_arm_command(rby.JointPositionCommandBuilder()
                             .set_minimum_time(5).set_position(np.zeros(len(model.left_arm_idx))))
   )
   feedback = robot.send_command(
       rby.RobotCommandBuilder().set_command(
           rby.ComponentBasedCommandBuilder().set_body_command(body)),
       1,  # priority
   ).get()  # Blocks until the command finishes.
   print(feedback.finish_code == rby.RobotCommandFeedback.FinishCode.Ok)

.. warning::

   This snippet moves the robot. Clear the area around the robot and keep the
   E-Stop within reach before you run it. See
   `E-Stop Basics <../../getting-started/estop-basics.md>`_.

.. rubric:: Sections

.. list-table::
   :header-rows: 1
   :widths: 20 34 46

   * - Section
     - Main types
     - Description
   * - :doc:`client/index`
     - ``create_robot``, ``Robot_*``, ``Model_*``, ``RobotState_*``
     - Robot entry points and model-specific control and state classes.
   * - :doc:`builders/index`
     - ``*CommandBuilder``
     - Command builders for body, arm, torso, head, and mobility, and how
       they nest.
   * - :doc:`feedback/index`
     - ``*CommandFeedback``
     - Feedback returned by submitted commands.
   * - :doc:`state/index`
     - ``RobotInfo``, ``JointState``, ``ControlManagerState``, ``Log``, ...
     - State and metadata types returned by the robot.
   * - :doc:`modules/index`
     - ``math``, ``upc``, ``dynamics``
     - Submodules for trajectory generation, user PC (UPC) devices, and dynamics.
   * - :doc:`utilities/index`
     - ``DynamixelBus``, print helpers
     - Utility helpers and print configuration.

.. toctree::
   :hidden:
   :maxdepth: 2

   client/index
   builders/index
   feedback/index
   state/index
   modules/index
   utilities/index
