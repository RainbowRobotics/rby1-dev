JointPositionCommandFeedback
============================

``rb::JointPositionCommandFeedback`` is the leaf feedback type for joint-space
position commands.

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
     - Report progress for a joint-position command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``time_based_progress() const``
     - Read completion progress based on scheduled time.
     - Useful for timeline-style monitoring.
   * - ``position_based_progress() const``
     - Read completion progress based on position convergence.
     - Useful when target tracking matters more than time.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Accessor
     - Unit / encoding
     - Notes
   * - ``time_based_progress()``
     - Dimensionless
     - Proto comments document the range as ``[0, 1]``.
   * - ``position_based_progress()``
     - Dimensionless
     - Proto comments document the range as ``(-inf, 1]``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointPositionCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-feedback`
- :doc:`torso-command-feedback`
- :doc:`head-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
