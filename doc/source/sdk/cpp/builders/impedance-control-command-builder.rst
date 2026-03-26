ImpedanceControlCommandBuilder
==============================

``rb::ImpedanceControlCommandBuilder`` expresses a task-space impedance request
around one transform target. Use it when you want frame-based compliance
without the larger Cartesian-impedance feature set.

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
     - Hold a transform target plus translation and rotation impedance weights.

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
   * - ``SetReferenceLinkName(...)`` and ``SetLinkName(...)``
     - Choose the reference and target links.
     - These define the task-space frame pair.
   * - ``SetTransformation(...)``
     - Set the desired transform.
     - This is the main target.
   * - ``SetTranslationWeight(...)``, ``SetRotationWeight(...)``,
       ``SetDampingRatio(...)``
     - Tune compliance and damping.
     - These shape how errors are penalized.

.. rubric:: Key Numeric Parameters

.. list-table::
   :header-rows: 1
   :widths: 32 18 50

   * - Method
     - Unit / encoding
     - Notes
   * - ``SetTransformation(T)``
     - ``SE(3)``
     - Translation is carried in meters and rotation is encoded in the
       transform's rotation block.
   * - ``SetTranslationWeight(weight)``
     - ``N/m``
     - Per-axis translational stiffness values.
   * - ``SetRotationWeight(weight)``
     - ``Nm/rad``
     - Per-axis rotational stiffness values.
   * - ``SetDampingRatio(damping_ratio)``
     - Dimensionless
     - Damping ratio used to build the Cartesian damping matrix.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::ImpedanceControlCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`arm-command-builder`
- :doc:`torso-command-builder`
- :doc:`cartesian-impedance-control-command-builder`

.. rubric:: Examples

- ``gravity_compensation.cpp``
