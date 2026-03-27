HeadCommandBuilder
==================

``rb::HeadCommandBuilder`` is the narrow head-scoped command wrapper. It exists
because the head path currently accepts one primitive mode: joint-position
control.

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
     - Wrap the head joint-position primitive.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - constructor from ``JointPositionCommandBuilder``
     - Construct the head command directly from a joint-position primitive.
     - This is the main use of this type.
   * - ``SetCommand(...)``
     - Replace the active head primitive.
     - Accepts ``JointPositionCommandBuilder`` only.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::HeadCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-builder`
- :doc:`joint-position-command-builder`

.. rubric:: Examples

- ``demo_motion.cpp``
