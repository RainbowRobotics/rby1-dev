math::SO3
=========

``rb::math::SO3`` provides rotation-matrix helpers for 3D orientation work. Use
it when you need rotation construction, conversion, exponential or logarithmic
maps, or projection back onto ``SO(3)``.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/so3.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::math``
   * - Kind
     - ``class``
   * - Primary role
     - Provide static helpers for 3D rotation operations.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``MatrixType``
     - Matrix representation used by the rotation helpers.
     - Returned by the construction methods on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Identity()``, ``Inverse(...)``, ``Projection(...)``
     - Create or sanitize rotation matrices.
     - Use ``Projection(...)`` after noisy numeric operations.
   * - ``RotX/Y/Z(...)`` and ``FromRPY(...)`` / ``ToRPY(...)``
     - Convert to or from standard axis-angle or roll-pitch-yaw forms.
     - Good entry point for user-facing rotations.
   * - ``FromQuaternion(...)`` / ``ToQuaternion(...)`` and Euler helpers
     - Convert between matrix and alternate orientation parameterizations.
     - Covers both quaternion and Euler-angle conventions.
   * - ``Exp(...)``, ``Log(...)``, ``Hat(...)``, ``Vec(...)``
     - Work in the Lie algebra and tangent space.
     - Useful in estimators and geometric controllers.
   * - ``Average(...)`` and axis getters
     - Average multiple rotations or inspect basis axes.
     - Convenient analysis utilities.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::math::SO3
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`math-se3`
- :doc:`math-se2`

.. rubric:: Examples

- ``so3.cpp`` is the direct example for this page.
