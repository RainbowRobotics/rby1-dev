SE2VelocityCommandBuilder
=========================

``rb::SE2VelocityCommandBuilder`` is the planar-base velocity primitive. It is
the natural fit for mobile-base requests expressed as planar translation plus
yaw rate.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_builder.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Hold a planar base velocity target and its limits.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)``
     - Attach shared header metadata.
     - Uses :doc:`command-header-builder`.
   * - ``SetVelocity(...)``
     - Set the planar linear and angular velocity command.
     - The main mobility payload.
   * - ``SetMinimumTime(...)`` and ``SetAccelerationLimit(...)``
     - Set timing and acceleration limits.
     - Useful for bounded base accelerations.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetMinimumTime(minimum_time)``
     - ``s``
     - Minimum ramp duration.
   * - ``SetVelocity(linear, angular)``
     - ``m/s``, ``rad/s``
     - ``linear`` is planar ``[vx, vy]``. ``angular`` is yaw rate.
   * - ``SetAccelerationLimit(linear, angular)``
     - ``m/s^2``, ``rad/s^2``
     - Maximum planar and yaw acceleration values.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::SE2VelocityCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`mobility-command-builder`
- :doc:`../models/math-se2`

.. rubric:: Examples

- ``mobility_command.cpp``
