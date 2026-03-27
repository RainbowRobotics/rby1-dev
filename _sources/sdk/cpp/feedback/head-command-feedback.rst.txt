HeadCommandFeedback
===================

``rb::HeadCommandFeedback`` is the small feedback branch for the head command
path.

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
     - Hold the feedback branch for the head joint-position command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``joint_position_command() const``
     - Access the head joint-position feedback leaf.
     - This is the only head feedback accessor.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::HeadCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`component-based-command-feedback`
- :doc:`joint-position-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
