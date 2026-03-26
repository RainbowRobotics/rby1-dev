OptimalControlCommandFeedback
=============================

``rb::OptimalControlCommandFeedback`` is the leaf feedback type for
optimal-control commands.

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
     - Report optimization costs for an optimal-control command.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``total_cost() const``
     - Read the total optimization cost.
     - This is the main scalar summary.
   * - ``center_of_mass_cost() const``
     - Read the COM objective cost.
     - Useful when COM tracking is active.
   * - ``joint_position_costs() const`` and ``cartesian_costs() const``
     - Read detailed cost breakdowns.
     - Useful when tuning target weights.

.. rubric:: Returned Values & Units

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Accessor
     - Unit / encoding
     - Notes
   * - ``total_cost()``
     - Dimensionless
     - Total objective value reported by the optimizer.
   * - ``cartesian_costs()``
     - Dimensionless
     - Per-target Cartesian cost terms.
   * - ``center_of_mass_cost()``
     - Dimensionless
     - COM objective contribution.
   * - ``joint_position_costs()``
     - Dimensionless
     - Per-joint position cost terms.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::OptimalControlCommandFeedback
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`torso-command-feedback`
- :doc:`body-command-feedback`
- :doc:`../models/optimal-control`

.. rubric:: Examples

- ``optimal_control.cpp``
