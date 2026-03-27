math::SE3
=========

``rb::math::SE3`` provides 3D rigid transform helpers. It is the natural
companion to ``SO3`` when controllers or planners need poses, twists, or
adjoint operators between reference frames.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/se3.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::math``
   * - Kind
     - ``class``
   * - Primary role
     - Provide static helpers for 3D rigid transforms and adjoint operations.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``MatrixType``
     - Matrix representation used by the transform helpers.
     - Returned by the construction methods on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Identity()``, ``T(...)``, ``Inverse(...)``
     - Create or invert rigid transforms.
     - ``T(...)`` builds transforms from position and rotation data.
   * - ``Exp(...)``, ``Log(...)``, ``Hat(...)``, ``Vec(...)``
     - Move between transform matrices and twist-space representations.
     - Common in model-based control and estimation.
   * - ``Ad(...)``, ``InvAd(...)``, ``ad(...)``, ``adTranspose(...)``
     - Apply adjoint and Lie-bracket operators.
     - Useful for wrench and twist transforms.
   * - ``GetPosition(...)``, ``GetRotation(...)``, ``Multiply(...)``
     - Extract components or apply a transform to a point.
     - Good for task-space utility code.
   * - ``Average(...)``
     - Average a set of rigid transforms.
     - Useful for pose filtering and alignment.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::math::SE3
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`math-so3`
- :doc:`dyn-inertial`

.. rubric:: Examples

- ``dynamics/load_urdf.cpp`` and ``optimal_control.cpp`` are good places to see
  ``SE3`` in context.
