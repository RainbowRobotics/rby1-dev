JogCommandBuilder
=================

``rb::JogCommandBuilder`` creates a named-joint jog request. It is separate
from the main body, head, or mobility builder trees because it addresses one
joint by name and one jog mode at a time.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_builder.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Hold a single named-joint jog command.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``AbsolutePosition``
     - Jog to an explicit absolute position.
     - One of the three jog modes.
   * - ``RelativePosition``
     - Jog by an offset from the current position.
     - Useful for operator-driven increments.
   * - ``OneStep``
     - Perform one incremental step.
     - In the C++ API this carries a direction flag; the public header does not
       expose a step magnitude.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)`` and ``SetJointName(...)``
     - Attach header metadata and choose the target joint.
     - Both are required for a meaningful jog request.
   * - ``SetCommand(...)``
     - Choose the jog mode.
     - Accepts ``AbsolutePosition``, ``RelativePosition``, or ``OneStep``.
   * - ``SetVelocityLimit(...)`` and ``SetAccelerationLimit(...)``
     - Bound the jog motion.
     - Useful in operator-facing tooling.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Method or value type
     - Unit / encoding
     - Notes
   * - ``SetVelocityLimit(value)``
     - ``rad/s``
     - Maximum joint velocity during the jog.
   * - ``SetAccelerationLimit(value)``
     - ``rad/s^2``
     - Maximum joint acceleration during the jog.
   * - ``AbsolutePosition(value)``
     - ``rad``
     - Absolute joint-angle target.
   * - ``RelativePosition(value)``
     - ``rad``
     - Relative joint-angle offset.
   * - ``OneStep(value)``
     - Direction flag
     - The C++ public header exposes ``bool value()``. A physical step size is
       not specified there.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JogCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-builder`

.. rubric:: Examples

- ``module_test/*`` utilities are the most relevant entry points for jog-style
  service flows.
