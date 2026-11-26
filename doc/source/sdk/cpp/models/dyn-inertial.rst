dyn::Inertial
=============

``rb::dyn::Inertial`` provides inertia-matrix constructors and transformation
helpers for rigid-body links. It is the low-level entry point when you need to
create, inspect, or move inertia tensors between frames.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/dynamics/inertial.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::dyn``
   * - Kind
     - ``class``
   * - Primary role
     - Construct and transform rigid-body inertia matrices.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``MatrixType``
     - Matrix representation used by the inertia helpers.
     - Passed into every factory and accessor on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``I(...)``
     - Build inertia matrices from mass, principal moments, or full inertia
       data.
     - Multiple overloads cover common construction patterns.
   * - ``GetMass(...)``, ``GetCOM(...)``, ``GetInertia(...)``
     - Extract physical values from an inertia matrix.
     - Useful when inspecting imported models.
   * - ``Transform(...)``
     - Move an inertia matrix through an ``SE3`` transform.
     - Frame-conversion helper for the same inertia data.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::dyn::Inertial
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dyn-link`
- :doc:`math-se3`

.. rubric:: Examples

- `dynamics/load_urdf.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/dynamics/load_urdf.cpp>`__: inertial data of a model loaded from URDF.
- `dynamics/sample_robot.h <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/dynamics/sample_robot.h>`__: builds links with ``Inertial`` values in code.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
