math::SE2
=========

``rb::math::SE2`` provides planar rigid transform helpers. It is most useful in
mobility and planar-base code where 2D poses and twists are enough.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/se2.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::math``
   * - Kind
     - ``class``
   * - Primary role
     - Provide static helpers for planar rigid transforms.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``MatrixType``
     - Matrix representation used by the planar-transform helpers.
     - Returned by the construction methods on this page.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Identity()`` and ``T(...)``
     - Create planar transforms.
     - ``T(...)`` combines heading and translation.
   * - ``Exp(...)`` and ``Log(...)``
     - Move between planar transforms and planar twist coordinates.
     - Useful for mobility control and estimation.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::math::SE2
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`math-se3`
- :doc:`../builders/se2-velocity-command-builder`

.. rubric:: Examples

- `37_mobile_test.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/37_mobile_test.cpp>`__: ``SE2`` values for mobile base velocity commands.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
