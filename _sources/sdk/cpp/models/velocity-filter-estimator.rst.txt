VelocityFilterEstimator
=======================

``rb::VelocityFilterEstimator`` estimates scalar velocity from sampled position
data. It is a lightweight utility class used in local filtering and example
code.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/math/velocity_estimator.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Estimate velocity with a short moving-window filter.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``VelocityFilterEstimator(...)``
     - Construct the estimator with a sample period and averaging window.
     - ``avg_count`` controls the smoothing window length.
   * - ``Update(...)``
     - Feed a new position sample into the estimator.
     - The ``valid`` flag lets callers skip invalid samples.
   * - ``GetVelocity()``
     - Read the estimated velocity.
     - Use after one or more ``Update(...)`` calls.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::VelocityFilterEstimator
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`trapezoidal-motion-generator`

.. rubric:: Examples

- ``velocity_estimation.cpp`` is the direct example for this page.
