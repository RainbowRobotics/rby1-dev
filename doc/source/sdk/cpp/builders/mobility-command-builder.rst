MobilityCommandBuilder
======================

``rb::MobilityCommandBuilder`` selects one mobility-scoped command mode. Use it
for wheel-joint velocity or planar-base velocity requests.

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
     - Wrap one mobility primitive command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - converting constructors
     - Construct directly from a joint-velocity or SE2-velocity primitive.
     - These are the only mobility primitives.
   * - ``SetCommand(...)``
     - Replace the active mobility primitive.
     - Use before inserting into ``ComponentBasedCommandBuilder``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::MobilityCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-builder`
- :doc:`joint-velocity-command-builder`
- :doc:`se2-velocity-command-builder`

.. rubric:: Examples

- `37_mobile_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/37_mobile_test.cpp>`__: mobility commands with SE(2) velocity control.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
