math::QPSolver
==============

``rb::math::QPSolver`` is the quadratic-programming helper used by advanced
control and optimization code. The related ``QPSolverException`` is documented
on this page because it is tightly coupled to solver setup and failure modes.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/qp_solver.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::math``
   * - Kind
     - ``class`` family
   * - Primary role
     - Configure and solve constrained quadratic programs.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Setup(...)`` and ``InitFunction()``
     - Allocate the solver and initialize its problem dimensions.
     - Call before setting cost or constraints.
   * - ``SetCostFunction(...)`` and ``AddCostFunction(...)``
     - Define one or more least-squares cost terms.
     - ``AddCostFunction(...)`` augments an existing cost.
   * - ``SetConstraintsFunction(...)`` and ``SetPrimalVariable(...)``
     - Define bound and constraint data plus the initial guess.
     - Needed before solving most nontrivial problems.
   * - ``Solve()``
     - Execute the QP solve.
     - May throw or return failure information via the paired exception type.
   * - ``Get*()`` accessors
     - Inspect the assembled matrices and bounds.
     - Useful for debugging a solver configuration.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::math::QPSolver
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::math::QPSolverException
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`optimal-control`
- :doc:`../builders/optimal-control-command-builder`

.. rubric:: Examples

- ``optimal_control.cpp`` is the main end-to-end example for this solver path.
