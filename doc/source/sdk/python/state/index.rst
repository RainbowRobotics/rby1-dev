State & Metadata
================

.. currentmodule:: rby1_sdk

Types that the robot returns: robot information, state snapshots of each
subsystem, Control Manager state, logs, and network and serial device records.
``RobotState_A``, ``RobotState_M`` and ``RobotState_UB`` (see :doc:`../client/index`)
contain the state types below.

Robot information
~~~~~~~~~~~~~~~~~

Returned by ``Robot_*.get_robot_info()``.

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   RobotInfo
   JointInfo
   BatteryInfo
   PowerInfo
   EMOInfo

State
~~~~~

Fields of ``RobotState_*``, returned by ``Robot_*.get_state()`` and passed to
the ``start_state_update()`` callback.

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   JointState
   BatteryState
   PowerState
   EMOState
   ToolFlangeState
   FTSensorData
   SystemStat

Control Manager, logs, and settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   ControlManagerState
   Log
   PIDGain
   Color

Network and serial devices
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   WifiNetwork
   WifiStatus
   SerialDevice
   SerialStream

Verified against: rby1-sdk v0.10.1 Python package (``dir(rby1_sdk)``),
``python/robot.cpp``, ``python/robot_info.cpp``, ``python/robot_state.cpp``,
``python/control_manager_state.cpp`` and ``python/log.cpp`` bindings.
