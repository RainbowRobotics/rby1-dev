DynamixelBus
============

``rb::DynamixelBus`` is the direct peripheral-access class for Dynamixel-based
devices. This page is intentionally close in spirit to ROBOTIS's own
``PortHandler``-style reference: open the bus, configure communication, then
read or write grouped or per-device values.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/base/dynamixel_bus.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Open a Dynamixel device bus and perform low-level read or write
       operations for attached devices.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``DynamixelBus(...)``, ``OpenPort()``, ``SetBaudRate(...)``
     - Configure the port and communication settings.
     - This is the bus bring-up sequence.
   * - ``Ping(...)`` and ``Read*()`` helpers
     - Check presence and read one device's state or configuration.
     - Covers encoder, torque-enable, operating mode, temperature, and buttons.
   * - ``GroupFastSyncRead*()`` and ``GetMotorStates(...)``
     - Read multiple devices efficiently in one transaction.
     - Use for synchronized state polling.
   * - ``Send*()`` and ``GroupSyncWrite*()``
     - Write torque, position, operating mode, or vibration values.
     - Use the grouped variants for multi-device updates.
   * - ``GetPosition*Gain()`` and ``SetPosition*Gain(...)``
     - Inspect or change PID gains.
     - Covers individual gains or the combined PID record.
   * - ``SetTorqueConstant(...)``
     - Configure torque constants used by the helper routines.
     - Useful when mapping current or torque values.

.. rubric:: Numeric Fields, Units & Encodings

.. list-table::
   :header-rows: 1
   :widths: 34 18 48

   * - Method or field family
     - Unit / encoding
     - Notes
   * - ``SetBaudRate(baudrate)``
     - Baud rate value
     - Serial line speed passed as an integer baud setting.
   * - ``ReadEncoder()``, ``GroupFastSyncReadEncoder()``,
       ``MotorState::position``
     - ``rad``
     - Encoder values converted into joint angle.
   * - ``MotorState::velocity``
     - ``rad/s``
     - Present motor velocity.
   * - ``SendCurrent(...)``, ``MotorState::current``
     - ``A``
     - Motor current command/readback.
   * - ``SendTorque(...)``, ``GroupSyncWriteSendTorque(...)``,
       ``MotorState::torque``
     - ``Nm``
     - Torque command/readback.
   * - ``ReadTemperature()``, ``MotorState::temperature``
     - ``deg C``
     - Motor temperature values.
   * - ``SendGoalPosition(...)``, ``GroupSyncWriteSendPosition(...)``
     - Encoder units
     - Public Python docs explicitly describe these as raw encoder units rather
       than radians.
   * - ``SetPosition*Gain(...)``, ``GetPosition*Gain(...)``,
       ``PIDGain::p_gain/i_gain/d_gain``
     - Register value
     - Raw PID register values, not normalized gains.
   * - ``ReadOperatingMode(...)``, ``SendOperatingMode(...)``,
       ``GroupSyncWriteOperatingMode(...)``
     - Register / enum value
     - Operating-mode encoding from the motor firmware.
   * - ``ReadTorqueEnable(...)``, ``GroupFastSyncReadTorqueEnable(...)``,
       ``GroupSyncWriteTorqueEnable(...)``
     - ``0`` / ``1``
     - Torque-enable flag values.
   * - ``ReadButtonStatus()`` / ``ButtonState::button``,
       ``ButtonState::trigger``
     - State value
     - Exposed as integer button/trigger states. No physical unit is defined.
   * - ``SendVibration(level)``
     - Range ``[0, 255]``
     - Raw vibration-level command.
   * - ``SetTorqueConstant(...)``
     - Not specified
     - Public C++/Python docs describe the parameter but do not assign a unit.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::DynamixelBus
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`master-arm`
- :doc:`network-utilities`

.. rubric:: Examples

- ``module_test/gripper.cpp``
- ``module_test/head.cpp``
- ``module_test/tool_flange.cpp``
