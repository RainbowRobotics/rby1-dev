dyn::Robot
==========

``rb::dyn::Robot`` is the main rigid-body model type in the SDK. It exposes the
kinematics and dynamics computations used by model-based control and offline
analysis tools.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/dynamics/robot.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::dyn``
   * - Kind
     - ``class template``
   * - Primary role
     - Own a robot model and compute forward kinematics, Jacobians, center of
       mass, gravity terms, mass matrices, and inverse dynamics.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Robot(...)`` and ``CountJoints(...)``
     - Construct a model and inspect link-tree size.
     - ``CountJoints(...)`` is the main static helper.
   * - ``ComputeForwardKinematics(...)`` and differential variants
     - Update link transforms and motion derivatives in a state object.
     - Use before Jacobian or body-velocity queries.
   * - ``ComputeBodyJacobian(...)`` and ``ComputeSpaceJacobian(...)``
     - Compute task-space Jacobians between links.
     - Common in controller and estimator code.
   * - ``ComputeCenterOfMass(...)`` and ``ComputeCenterOfMassJacobian(...)``
     - Compute COM position and Jacobians.
     - Supports whole robot or selected target links.
   * - ``ComputeGravityTerm(...)``, ``ComputeMassMatrix(...)``,
       ``ComputeInverseDynamics(...)``
     - Compute the main dynamics terms.
     - These are the standard model-based control outputs.
   * - ``ComputeMass(...)`` and ``ComputeReflectiveInertia(...)``
     - Inspect local reflected mass and inertia quantities.
     - Useful for analysis and tuning.
   * - ``ComputeMobility*`` helpers
     - Map planar mobility commands through the model.
     - Relevant for mobile-base variants.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::dyn::Robot
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dyn-state`
- :doc:`dyn-link`
- :doc:`model-descriptors`

.. rubric:: Examples

- ``dynamics/load_urdf.cpp``
- ``dynamics/mass_matrix.cpp``
- ``dynamics/inverse_dynamics.cpp``
