dyn::State
==========

``rb::dyn::State`` is the mutable state container passed into the rigid-body
model computations. It stores joint vectors, intermediate kinematic quantities,
and base-motion terms used by the dynamics layer.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/dynamics/state.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::dyn``
   * - Kind
     - ``class template``
   * - Primary role
     - Hold joint vectors, gravity, base twist, and intermediate dynamic state.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Field group
     - Meaning
     - Notes
   * - ``q``, ``qdot``, ``qddot``, ``tau``
     - Joint position, velocity, acceleration, and torque vectors.
     - The main dynamic inputs and outputs.
   * - ``T``, ``V``, ``Vdot``, ``S``, ``E``, ``F``
     - Intermediate rigid-body quantities.
     - Mostly useful after model computations run.
   * - ``V0`` and ``Vdot0``
     - Base motion terms.
     - Relevant for floating-base or moving-base setups.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``GetQ*()``, ``GetTau()``, ``GetV0()``, ``GetVdot0()``
     - Read the main state vectors.
     - Useful when state is owned by another subsystem.
   * - ``SetQ*()``, ``SetTau()``, ``SetV0()``, ``SetVdot0()``, ``SetGravity(...)``
     - Write the main state vectors and gravity.
     - Call before running model computations.
   * - ``GetJointNames()``, ``GetLinkNames()``, ``GetBaseLinkIdx()``
     - Inspect the model-index mapping bound into the state.
     - Useful for debugging and analysis.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::dyn::State
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dyn-robot`
- :doc:`dyn-link`
- :doc:`dyn-joint`

.. rubric:: Examples

- ``dynamics/load_urdf.cpp``
- ``dynamics/gravity_term.cpp``
