BodyComponentBasedCommandBuilder
================================

``rb::BodyComponentBasedCommandBuilder`` splits a body command into separate
left-arm, right-arm, and torso branches. Use it when the torso and the two arms
must each run their own command mode in one outer request.

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
     - Compose torso and arm commands inside one body command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetLeftArmCommand(...)``
     - Attach the left-arm subtree.
     - Accepts ``ArmCommandBuilder``.
   * - ``SetRightArmCommand(...)``
     - Attach the right-arm subtree.
     - Accepts ``ArmCommandBuilder``.
   * - ``SetTorsoCommand(...)``
     - Attach the torso subtree.
     - Accepts ``TorsoCommandBuilder``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::BodyComponentBasedCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-command-builder`
- :doc:`arm-command-builder`
- :doc:`torso-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``gravity_compensation.cpp``
