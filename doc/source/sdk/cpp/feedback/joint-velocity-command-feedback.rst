JointVelocityCommandFeedback
============================

``rb::JointVelocityCommandFeedback`` is the leaf feedback type for joint-space
velocity commands.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_feedback.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Mark the leaf result for a joint-velocity command.

.. rubric:: Public Member Functions

- No type-specific methods are added at this leaf. Use the inherited validity
  and completion checks from the base feedback classes.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointVelocityCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`mobility-command-feedback`

.. rubric:: Examples

- ``mobility_command.cpp``
