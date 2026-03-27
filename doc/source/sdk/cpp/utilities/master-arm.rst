MasterArm
=========

``rb::upc::MasterArm`` is the SDK-side helper for the RB-Y1 master-arm device.
It wraps device initialization, torque management, and a local control loop
around the master-arm hardware.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/upc/master_arm.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::upc``
   * - Kind
     - ``class``
   * - Primary role
     - Manage master-arm initialization, torque, and callback-driven control.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``MasterArm(...)`` and ``Initialize(...)``
     - Construct and initialize the device.
     - Initialization is the required bring-up step.
   * - ``EnableTorque()`` and ``DisableTorque()``
     - Turn master-arm torque on or off.
     - Common in startup and shutdown flow.
   * - ``SetControlPeriod(...)``, ``SetModelPath(...)``,
       ``SetTorqueConstant(...)``
     - Configure control timing and model constants.
     - Use before entering control.
   * - ``StartControl(...)`` and ``StopControl(...)``
     - Run or stop the master-arm control callback.
     - ``StopControl(...)`` can optionally disable torque.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::upc::MasterArm
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dynamixel-bus`
- :doc:`../client/robot`

.. rubric:: Examples

- ``demo_motion_with_master_arm.cpp``
- ``module_test/master_arm.cpp``
- ``teleoperation_with_joint_mapping.cpp``
