LeaderArm
=========

``rb::upc::LeaderArm`` is the SDK-side helper for the RB-Y1 leader-arm device
(the teleoperation input device, formerly called the master arm).
It wraps device initialization, torque management, and a local control loop
around the leader-arm hardware.

.. note::

   Since rby1-sdk v0.10.0 the class is ``LeaderArm`` and the header is
   ``rby1-sdk/upc/leader_arm.h``. ``rb::upc::MasterArm`` and
   ``rby1-sdk/upc/master_arm.h`` remain as deprecated aliases.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/upc/leader_arm.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::upc``
   * - Kind
     - ``class``
   * - Primary role
     - Manage leader-arm initialization, torque, and callback-driven control.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``LeaderArm(...)`` and ``Initialize(...)``
     - Construct and initialize the device.
     - Initialization is the required bring-up step. With an empty
       ``dev_name`` (the default) or ``kLeaderArmDeviceName``, the constructor
       uses ``ResolveLeaderArmDeviceName()``.
   * - ``EnableTorque()`` and ``DisableTorque()``
     - Turn leader-arm torque on or off.
     - Common in startup and shutdown flow.
   * - ``SetControlPeriod(...)``, ``SetModelPath(...)``,
       ``SetTorqueConstant(...)``
     - Configure control timing and model constants.
     - Use before entering control.
   * - ``StartControl(...)`` and ``StopControl(...)``
     - Run or stop the leader-arm control callback.
     - ``StopControl(...)`` can optionally disable torque.

.. rubric:: Device Names

Defined in ``#include <rby1-sdk/upc/device.h>`` (namespace ``rb::upc``). The
user PC (UPC) udev rules create these device links.

.. list-table::
   :header-rows: 1
   :widths: 36 30 34

   * - Name
     - Value
     - Notes
   * - ``kLeaderArmDeviceName``
     - ``"/dev/rby1_leader_arm"``
     - Current leader arm device link.
   * - ``kLegacyLeaderArmDeviceName``
     - ``"/dev/rby1_master_arm"``
     - Device link of older udev rules.
   * - ``kMasterArmDeviceName``
     - same as ``kLeaderArmDeviceName``
     - Deprecated. Use ``kLeaderArmDeviceName``.
   * - ``kGripperDeviceName``
     - ``"/dev/rby1_gripper"``
     - Gripper device link.
   * - ``ResolveLeaderArmDeviceName()``
     - function
     - Returns ``kLeaderArmDeviceName`` if that device exists. Otherwise, if
       ``kLegacyLeaderArmDeviceName`` exists, prints a warning to update the
       udev rules and returns it. If neither exists, returns
       ``kLeaderArmDeviceName``.
   * - ``InitializeDevice(device_name)``
     - function
     - Sets the USB serial latency timer of the device to 1 ms. Empty or
       ``kLeaderArmDeviceName`` is resolved as above. Throws
       ``std::runtime_error`` if the latency timer cannot be written. Not
       available on Windows.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::upc::LeaderArm
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dynamixel-bus`
- :doc:`../client/robot`

.. rubric:: Examples

- `20_leader_arm_state_check.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/20_leader_arm_state_check.cpp>`__: initializes the leader arm and runs its control loop. Not supported in simulation.
- `35_leader_arm_teleop_with_monitor.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/35_leader_arm_teleop_with_monitor.cpp>`__: teleoperation with the leader arm and the grippers. Not supported in simulation.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
