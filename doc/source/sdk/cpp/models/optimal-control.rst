OptimalControl
==============

``rb::OptimalControl`` is the runtime solver object behind the SDK's
optimal-control workflow. It is separate from the command builder: this page
covers the solver itself and the nested target records it consumes.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/optimal_control.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class template``
   * - Primary role
     - Solve constrained model-based control problems against a dynamics model.

.. rubric:: Member Types / Enums

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``ExitCode``
     - Solver exit status.
     - Check after each call to ``Solve(...)``.
   * - ``Input`` and target structs
     - Bundle COM, link, joint-angle, and nullspace targets.
     - These records define the actual optimization problem.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``OptimalControl(...)``
     - Construct the solver for one robot model and joint subset.
     - Binds the solver to a dynamics model.
   * - ``Solve(...)``
     - Run the optimal-control solve.
     - Overloads cover bounded and unbounded position-limit cases.
   * - ``GetExitCode*()``, ``GetError()``, ``GetManipulability()``
     - Inspect the result of the most recent solve.
     - Use for diagnostics and controller tuning.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::OptimalControl
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`math-qp-solver`
- :doc:`dyn-robot`
- :doc:`../builders/optimal-control-command-builder`

.. rubric:: Examples

- ``optimal_control.cpp`` is the direct example for this page.
