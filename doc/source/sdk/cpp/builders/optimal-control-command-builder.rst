OptimalControlCommandBuilder
============================

``rb::OptimalControlCommandBuilder`` describes an optimal-control request that
will be solved by the robot-side optimal-control path. It is the command-layer
counterpart to :doc:`../models/optimal-control`.

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
     - Hold optimal-control targets and solver tuning parameters.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)``
     - Attach shared header metadata.
     - Uses :doc:`command-header-builder`.
   * - ``AddCartesianTarget(...)`` and ``AddJointPositionTarget(...)``
     - Add task-space and joint-space objectives.
     - These define most of the optimization goal.
   * - ``SetCenterOfMassTarget(...)``
     - Add a COM objective.
     - Useful for balance or posture tasks.
   * - ``SetVelocityLimitScaling(...)``, ``SetAccelerationLimitScaling(...)``,
       ``SetErrorScaling(...)``
     - Tune scaling applied to the optimization problem.
     - Useful when adapting solver aggressiveness.
   * - ``SetPatience(...)`` and ``SetStopCost(...)``
     - Tune solver termination behavior.
     - Useful during iterative optimization tuning.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 34 18 48

   * - Method
     - Unit / encoding
     - Notes
   * - ``AddCartesianTarget(..., T, translation_weight, rotation_weight)``
     - ``SE(3)``, Dimensionless
     - ``T`` carries translation in meters. The two weights are objective
       weights.
   * - ``SetCenterOfMassTarget(..., pose, weight)``
     - ``m``, Dimensionless
     - COM target position is a 3-vector in meters.
   * - ``AddJointPositionTarget(..., target_position, weight)``
     - ``rad``, Dimensionless
     - Joint-space target plus its objective weight.
   * - ``SetErrorScaling(...)``, ``SetVelocityLimitScaling(...)``,
       ``SetAccelerationLimitScaling(...)``
     - Dimensionless
     - Internal optimization scalings. Proto comments document positive ranges
       for the limit-scaling terms.
   * - ``SetStopCost(...)``, ``SetMinDeltaCost(...)``
     - Dimensionless
     - Objective thresholds used by solver termination logic.
   * - ``SetPatience(patience)``
     - Iteration count
     - Number of iterations tolerated without sufficient improvement.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::OptimalControlCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`body-command-builder`
- :doc:`torso-command-builder`
- :doc:`../models/optimal-control`

.. rubric:: Examples

- `24_demo_motion.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/24_demo_motion.cpp>`__: optimal control step of the demo sequence.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
