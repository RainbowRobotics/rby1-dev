Model & Math API
================

These pages cover compile-time model descriptors, rigid-body dynamics, Lie-group
math, solvers, and motion-profile helpers. Open this category when you are
working with model-based control or offline analysis tooling.

.. rubric:: API Pages

.. list-table::
   :header-rows: 1
   :widths: 28 30 42

   * - Page
     - Main types
     - Description
   * - :doc:`model-descriptors`
     - ``rb::y1_model::A``, ``M``, ``UB``
     - Compile-time robot constants such as DOF, joint ordering, and subsystem
       index groups.
   * - :doc:`dyn-robot`
     - ``rb::dyn::Robot``
     - Forward kinematics, Jacobians, mass matrices, gravity terms, and inverse
       dynamics.
   * - :doc:`dyn-state`
     - ``rb::dyn::State``
     - Dynamic state container passed into model computations.
   * - :doc:`dyn-link`
     - ``rb::dyn::Link``
     - Link and collision objects used inside a model tree.
   * - :doc:`dyn-joint`
     - ``rb::dyn::Joint``
     - Joint factories, link connections, and joint-limit metadata.
   * - :doc:`dyn-inertial`
     - ``rb::dyn::Inertial``
     - Rigid-body inertia matrix construction and frame transforms.
   * - :doc:`math-so3`
     - ``rb::math::SO3``
     - Rotation construction, conversion, and logarithmic maps.
   * - :doc:`math-se3`
     - ``rb::math::SE3``
     - 3D pose transforms and adjoint operations.
   * - :doc:`math-se2`
     - ``rb::math::SE2``
     - Planar pose transforms for base and mobility math.
   * - :doc:`math-qp-solver`
     - ``rb::math::QPSolver``
     - Constrained quadratic optimization helpers.
   * - :doc:`optimal-control`
     - ``rb::OptimalControl``
     - Runtime optimal-control solver interface.
   * - :doc:`trapezoidal-motion-generator`
     - ``rb::TrapezoidalMotionGenerator``
     - Local trapezoidal motion-profile generator.
   * - :doc:`velocity-filter-estimator`
     - ``rb::VelocityFilterEstimator``
     - Filtered scalar velocity estimation from sampled positions.

.. toctree::
   :hidden:

   model-descriptors
   dyn-robot
   dyn-state
   dyn-link
   dyn-joint
   dyn-inertial
   math-so3
   math-se3
   math-se2
   math-qp-solver
   optimal-control
   trapezoidal-motion-generator
   velocity-filter-estimator
