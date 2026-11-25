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
     - Initialization is the required bring-up step.
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

.. rubric:: Detailed Reference

.. doxygenclass:: rb::upc::LeaderArm
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dynamixel-bus`
- :doc:`../client/robot`

.. rubric:: Examples

- ``examples/cpp/20_leader_arm_state_check.cpp``
- ``examples/cpp/35_leader_arm_teleop_with_monitor.cpp``
