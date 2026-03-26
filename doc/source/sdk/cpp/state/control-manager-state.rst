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
     - Relevant when enabling the manager with unlimited mode.

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

- ``demo_motion.cpp`` and ``power_command.cpp`` both pass through the
  control-manager lifecycle.
