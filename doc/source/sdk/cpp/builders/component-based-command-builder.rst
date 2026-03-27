ComponentBasedCommandBuilder
============================

``rb::ComponentBasedCommandBuilder`` composes commands across major robot
subsystems. Use it when one request must contain body, head, or mobility
commands together.

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
     - Compose body, head, and mobility subcommands into one request.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetBodyCommand(...)``
     - Attach the body command subtree.
     - Usually the largest part of the request.
   * - ``SetHeadCommand(...)``
     - Attach a head command.
     - Typically a joint-position request.
   * - ``SetMobilityCommand(...)``
     - Attach a mobility command.
     - Useful for mobile-base variants.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ComponentBasedCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot-command-builder`
- :doc:`body-command-builder`
- :doc:`head-command-builder`
- :doc:`mobility-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
- ``mobility_command.cpp``
