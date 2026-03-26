JointGroupPositionCommandFeedback
=================================

``rb::JointGroupPositionCommandFeedback`` is the leaf feedback type for
named-subset joint-position commands.

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
     - Report progress for a joint-group position command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``joint_indices() const``
     - Read the addressed joint indices.
     - Useful when a subset command is handled generically.
   * - ``time_based_progress() const``
     - Read completion progress based on scheduled time.
     - Useful for time-based monitoring.
   * - ``position_based_progress() const``
     - Read completion progress based on position convergence.
     - Useful for target-based monitoring.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Accessor
     - Unit / encoding
     - Notes
   * - ``joint_indices()``
     - Joint indices
     - Model-order indices for the addressed joint subset.
   * - ``time_based_progress()``
     - Dimensionless
     - Proto comments document the range as ``[0, 1]``.
   * - ``position_based_progress()``
     - Dimensionless
     - Proto comments document the range as ``(-inf, 1]``.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::JointGroupPositionCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`torso-command-feedback`

.. rubric:: Examples

- ``demo_motion.cpp``
