TrapezoidalMotionGenerator
==========================

``rb::TrapezoidalMotionGenerator`` provides a local motion-profile generator for
scalar or vector trajectories. It is a utility layer often used in examples and
controller support code rather than through the high-level robot client.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/trapezoidal_motion_generator.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Generate trapezoidal motion profiles and evaluate them over time.

.. rubric:: Member Types

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type
     - Purpose
     - Notes
   * - ``Input``
     - Motion-profile input record.
     - Passed into ``Update(...)``.
   * - ``Output``
     - Sampled output record at a given time.
     - Returned by ``operator()`` and ``at_time(...)``.
   * - ``Coeff``
     - Internal coefficient record for the profile.
     - Mainly useful during inspection or debugging.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Update(...)``
     - Load a new motion-profile request.
     - Replaces the active profile.
   * - ``operator()(...)`` and ``at_time(...)``
     - Sample the profile at a given time.
     - ``operator()(...)`` is the convenience form.
   * - ``GetTotalTime()``, ``GetLastInput()``, ``IsReached(...)``
     - Inspect profile duration, cached input, and completion state.
     - Useful in time-stepped loops.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::TrapezoidalMotionGenerator
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`velocity-filter-estimator`

.. rubric:: Examples

- ``trapezoidal_motion_generator.cpp`` is the direct example for this page.
