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
   * - ``BrakeRelease()`` and ``BrakeEngage()``
     - Release or engage the brakes of the joints that match the name pattern.
     - Service use only. A released joint can move under gravity. Read the
       Safety Notes below first.
   * - ``EnableControlManager()``, ``DisableControlManager()``,
       ``ResetFaultControlManager()``, ``WaitForControlReady()``
     - Control the execution subsystem and clear control-manager faults.
     - Check :doc:`../state/control-manager-state` first when faults are active.
       ``EnableControlManager(true)`` turns on unlimited mode; read the
       Safety Notes below first.
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
     - ``Control()`` runs the UDP-based real-time control loop and **blocks**
       until the callback returns ``finish = true`` (returns ``true``) or an
       error or abort ends it (returns ``false``). ``CancelControl()`` cancels
       the running control.
     - Uses :doc:`control-loop-types`.
   * - ``GetParameter*()``, ``SetParameter*()``, ``ResetParameter*()``
     - Inspect, set, or reset named configuration parameters.
     - Includes full reset and factory reset helpers.
   * - ``ConnectWifi()``, ``ScanWifi()``, ``OpenSerialStream(...)``,
       ``ResetOdometry(...)``
     - Cover networking, serial-device access, and mobility-adjacent utilities.
     - These are secondary but still part of the public client.

.. rubric:: Typical Flow

The motion examples in rby1-sdk follow these steps (``InitializeRobot()`` and
``MoveJ()`` in ``examples/cpp/00_helper.cpp``): connect, power on, servo on,
reset a Control Manager fault if there is one, enable the Control Manager, send
a command, and wait for its feedback.

.. code-block:: cpp

   #include "rby1-sdk/model.h"
   #include "rby1-sdk/robot.h"
   #include "rby1-sdk/robot_command_builder.h"

   using namespace rb;

   int main() {
     using Model = y1_model::A;
     auto robot = Robot<Model>::Create("192.168.30.1:50051");
     if (!robot->Connect()) return 1;

     // ".*" is a regex that matches every device.
     if (!robot->IsPowerOn(".*") && !robot->PowerOn(".*")) return 1;
     if (!robot->IsServoOn(".*") && !robot->ServoOn(".*")) return 1;

     const auto cms = robot->GetControlManagerState();
     if (cms.state == ControlManagerState::State::kMajorFault ||
         cms.state == ControlManagerState::State::kMinorFault) {
       if (!robot->ResetFaultControlManager()) return 1;
     }
     if (!robot->EnableControlManager()) return 1;

     // Move the torso and both arms to the zero pose in at least 5 s. This moves the robot.
     Eigen::VectorXd q = Eigen::VectorXd::Zero(Model::kBodyIdx.size());
     auto handler = robot->SendCommand(RobotCommandBuilder().SetCommand(
         ComponentBasedCommandBuilder().SetBodyCommand(
             JointPositionCommandBuilder().SetPosition(q).SetMinimumTime(5.0))));

     const auto feedback = handler->Get();  // Blocks until the command finishes.
     return feedback.finish_code() == RobotCommandFeedback::FinishCode::kOk ? 0 : 1;
   }

.. warning::

   This snippet moves the robot. Clear the area around the robot and keep the
   E-Stop within reach before you run it. See
   `E-Stop Basics <../../../getting-started/estop-basics.md>`_.

.. rubric:: Safety Notes

.. danger::

   ``BrakeRelease(dev_name)`` releases the brakes of every joint whose name
   matches the regex ``dev_name``. A joint with a released brake and no servo
   torque can move or drop under gravity. ``".*"`` matches every joint,
   including the torso. Use it only for service work: start from a safe
   posture, release one joint at a time, support the link if needed, and call
   ``BrakeEngage()`` afterwards. The SDK example ``36_brake_test.cpp`` refuses
   torso joints and ``".*"`` for this reason.

.. warning::

   ``EnableControlManager(true)`` enables **unlimited mode**. In this mode the
   robot skips the joint position limit check when the Control Manager is
   enabled, and jog commands are not clamped to the joint limits. Use it only
   to recover a joint that is outside its limits, with slow motions and the
   E-Stop within reach. Use the default ``EnableControlManager()`` (``false``)
   for normal operation. ``ControlManagerState::unlimited_mode_enabled``
   shows the current mode.

.. warning::

   ``PowerOff()`` and ``ServoOff()`` stop motor control of the matching
   devices. Stop running commands and bring the robot to a safe, supported
   posture before you call them.

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

.. rubric:: Color

``rb::Color`` is the argument of ``SetLEDColor()``. ``r``, ``g`` and ``b`` are
8-bit channel values in ``[0, 255]``.

.. doxygenstruct:: rb::Color
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`serial-stream` (``SerialDevice``, ``SerialStream``)
- :doc:`robot-command-handler`
- :doc:`robot-command-stream-handler`
- :doc:`control-loop-types`
- :doc:`../builders/robot-command-builder`

.. rubric:: Examples

- `01_hello_rby1.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/01_hello_rby1.cpp>`__: connect and read ``RobotInfo``.
- `03_robot_state.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/03_robot_state.cpp>`__: power on and read one state snapshot.
- `05_robot_state_stream.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/05_robot_state_stream.cpp>`__: state updates with ``StartStateUpdate()``.
- `07_power.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/07_power.cpp>`__: ``PowerOn()`` and ``PowerOff()``.
- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: full power, servo, control manager and command cycle.
- `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__: the ``Control()`` real-time path.
- `36_brake_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/36_brake_test.cpp>`__: ``BrakeRelease()`` and ``BrakeEngage()`` on one joint.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
