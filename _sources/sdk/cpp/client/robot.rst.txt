Robot
=====

``rb::Robot<T>`` is the main application-facing client in the SDK. It owns the
network session to the robot and exposes the operational flow most user code
follows: connect, power and servo devices, enable the control manager, submit
commands, and read state or logs.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class template``
   * - Template parameter
     - ``T`` is one of the model descriptors from :doc:`../models/model-descriptors`.
   * - Primary role
     - Own the robot connection, state streams, command submission, time sync,
       parameters, and advanced real-time control entry points.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``Create(...)``, ``Connect(...)``, ``Disconnect()``, ``IsConnected()``
     - Construct the client and manage the robot connection lifecycle.
     - ``Create()`` is the usual entry point.
   * - ``GetRobotInfo()``, ``GetRobotModel()``, ``GetDynamics(...)``
     - Retrieve static metadata, the imported model, or a dynamics helper.
     - Use before building model-based control logic.
   * - ``PowerOn()``, ``PowerOff()``, ``ServoOn()``, ``ServoOff()``
     - Manage device power and servo state.
     - Device names accept regex-style patterns.
   * - ``BreakRelease()`` and ``BreakEngage()``
     - Manage brakes on the selected devices.
     - Useful in bring-up and service workflows.
   * - ``EnableControlManager()``, ``DisableControlManager()``,
       ``ResetFaultControlManager()``, ``WaitForControlReady()``
     - Control the execution subsystem and clear control-manager faults.
     - Check :doc:`../state/control-manager-state` first when faults are active.
   * - ``SendCommand(...)`` and ``CreateCommandStream(...)``
     - Submit one-shot commands or open a command stream.
     - Use :doc:`../builders/index` to construct the payload.
   * - ``StartStateUpdate(...)``, ``StopStateUpdate()``, ``GetState()``
     - Receive or poll live state snapshots.
     - See :doc:`../state/robot-state`.
   * - ``StartLogStream(...)``, ``StopLogStream()``, ``GetLastLog(...)``
     - Receive or fetch structured logs from the robot.
     - See :doc:`../state/log`.
   * - ``Control(...)`` and ``CancelControl()``
     - Enter or leave the UDP-based real-time control path.
     - Uses :doc:`control-loop-types`.
   * - ``GetParameter*()``, ``SetParameter*()``, ``ResetParameter*()``
     - Inspect, set, or reset named configuration parameters.
     - Includes full reset and factory reset helpers.
   * - ``ConnectWifi()``, ``ScanWifi()``, ``OpenSerialStream(...)``,
       ``ResetOdometry(...)``
     - Cover networking, serial-device access, and mobility-adjacent utilities.
     - These are secondary but still part of the public client.

.. rubric:: Numeric Parameters & Returns

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Method or family
     - Unit / encoding
     - Notes
   * - ``Connect(max_retries, timeout_ms)``
     - Retries, ``ms``
     - ``max_retries`` is a retry count. ``timeout_ms`` is the per-attempt
       connection timeout.
   * - ``GetTimeScale()``, ``SetTimeScale(...)``
     - Dimensionless
     - Motion-time scaling factor.
   * - ``SetPosition*Gain(...)``, ``Get*PositionPIDGain*()``
     - Register value
     - ``PIDGain::p_gain``, ``i_gain``, and ``d_gain`` are raw ``uint16``
       values, not SI units.
   * - ``SetToolFlangeOutputVoltage(...)``
     - ``V``
     - Common values called out by the headers are ``0``, ``12``, and ``24``.
   * - ``StartStateUpdate(..., rate)``, ``StartLogStream(..., rate)``
     - ``Hz``
     - Callback frequency requested from the robot.
   * - ``Control(..., port, priority)``
     - Port number, priority
     - ``port`` is a UDP port number. ``priority`` is an integer scheduling
       priority/command priority, not a physical unit.
   * - ``ResetOdometry(angle, position)``
     - ``rad``, ``m``
     - ``angle`` is the planar heading reset. ``position`` carries ``[x, y]``
       in meters.
   * - ``StartTimeSync(period_sec)``
     - ``s``
     - Period between time-synchronization attempts.
   * - ``SetLEDColor(color, duration, transition_time, blinking_freq)``
     - ``[0,255]``, ``s``, ``Hz``
     - ``Color::r/g/b`` are 8-bit channel values. Duration and transition are
       in seconds; blink frequency is in hertz.
   * - ``SetBatteryLevel(level)``
     - ``%``
     - Public headers document the battery-level range as ``0.0`` to ``100.0``.
   * - ``SetBatteryConfig(cutoff_voltage, fully_charged_voltage)``
     - ``V``
     - Battery cutoff and full-charge thresholds.
   * - ``WaitForControlReady(timeout_ms)``
     - ``ms``
     - Timed wait before control commands are accepted.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::Robot
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-handler`
- :doc:`robot-command-stream-handler`
- :doc:`control-loop-types`
- :doc:`../builders/robot-command-builder`

.. rubric:: Examples

- ``get_robot_state.cpp`` for the smallest connection and state flow.
- ``demo_motion.cpp`` for a full connect-power-servo-command cycle.
- ``real_time_control_command.cpp`` for the advanced ``Control()`` path.
