ArmCommandBuilder
=================

``rb::ArmCommandBuilder`` selects one arm-scoped command mode. It is the leaf
composition type used for the left or right arm within a split body command.

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
     - Wrap one arm-scoped primitive command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - converting constructors
     - Construct directly from one arm primitive.
     - Supports joint-position, cartesian, impedance, and gravity-compensation
       primitives.
   * - ``SetCommand(...)``
     - Replace the active primitive arm command.
     - Use before inserting into ``BodyComponentBasedCommandBuilder``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ArmCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-component-based-command-builder`
- :doc:`joint-position-command-builder`
- :doc:`cartesian-command-builder`
- :doc:`impedance-control-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``gravity_compensation.cpp``
