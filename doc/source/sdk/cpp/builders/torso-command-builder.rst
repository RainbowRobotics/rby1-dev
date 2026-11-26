TorsoCommandBuilder
===================

``rb::TorsoCommandBuilder`` selects one torso-scoped command mode. It supports
the broadest set of body primitives because torso motion can be driven by joint
groups, Cartesian targets, impedance, gravity compensation, or optimal control.

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
     - Wrap one torso-scoped primitive command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - converting constructors
     - Construct directly from one torso primitive.
     - Supports joint-position, joint-group-position, cartesian, impedance,
       gravity-compensation, and optimal-control builders.
   * - ``SetCommand(...)``
     - Replace the active torso primitive command.
     - Use before inserting into ``BodyComponentBasedCommandBuilder``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::TorsoCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-component-based-command-builder`
- :doc:`joint-group-position-command-builder`
- :doc:`optimal-control-command-builder`

.. rubric:: Examples

- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: torso joint position, Cartesian and optimal control commands.
- `30_joint_group_command.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/30_joint_group_command.cpp>`__: joint group command on the torso.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
