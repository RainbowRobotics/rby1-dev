ControlManagerState
===================

``rb::ControlManagerState`` describes the execution subsystem that sits between
the client and command execution. Read it before commanding the robot, and
check it again whenever a fault or execution transition is suspected.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/control_manager_state.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``struct``
   * - Primary role
     - Describe control-manager state, control execution state, enabled joints,
       and time-scale settings.

.. rubric:: Member Types / Enums

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``State``
     - High-level control-manager state.
     - Use it to distinguish idle, enabled, and fault modes.
   * - ``ControlState``
     - Execution-phase state for the current command path.
     - Useful while a command is starting, running, or switching.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Field
     - Meaning
     - Notes
   * - ``state``
     - Top-level control-manager state.
     - Check this first when diagnosing faults.
   * - ``control_state``
     - Execution-phase state.
     - Helps interpret transient command behavior.
   * - ``enabled_joint_idx``
     - Joint indices currently enabled by the manager.
     - Useful for partial-robot workflows.
   * - ``time_scale``
     - Active motion time scale.
     - Mirrors client-side time-scale control.
   * - ``unlimited_mode_enabled``
     - Whether unlimited mode is active.
     - Set by ``Robot::EnableControlManager(true)``. Should be ``false`` in
       normal operation; see the warning below.

.. warning::

   In unlimited mode the robot skips the joint position limit check when the
   Control Manager is enabled, and jog commands are not clamped to the joint
   limits. Use it only to recover a joint that is outside its limits, with slow
   motions and the E-Stop within reach. See
   `E-Stop Basics <../../../getting-started/estop-basics.md>`_.

.. rubric:: Numeric Fields & Encodings

.. list-table::
   :header-rows: 1
   :widths: 32 20 48

   * - Field
     - Unit / encoding
     - Notes
   * - ``time_scale``
     - Dimensionless
     - Multiplier applied to motion timing.
   * - ``enabled_joint_idx``
     - Joint indices
     - Model-order joint indices currently enabled by the control manager.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::ControlManagerState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`robot-state`
- :doc:`../feedback/robot-command-feedback`

.. rubric:: Examples

- `00_helper.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/00_helper.cpp>`__: reads the state and resets a fault before ``EnableControlManager()``.
- `20_leader_arm_state_check.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/20_leader_arm_state_check.cpp>`__: disables the control manager before leader arm control.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
