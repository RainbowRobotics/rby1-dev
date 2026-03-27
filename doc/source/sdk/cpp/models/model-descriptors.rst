Model Descriptors
=================

The ``rb::y1_model`` classes provide compile-time constants for the supported
RB-Y1 model families. Use these descriptors as the template parameter for
``rb::Robot<T>`` and for any data structure that depends on model-specific DOF
or joint ordering.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/model.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::y1_model``
   * - Kind
     - ``class`` family
   * - Primary role
     - Expose compile-time robot constants such as DOF and subsystem index
       groups.

.. rubric:: Public Types

.. list-table::
   :header-rows: 1
   :widths: 22 18 28 32

   * - Type
     - DOF
     - Main constants
     - Description
   * - ``A``
     - 24
     - body, arms, head, and mobility index groups
     - Full mobile manipulator model descriptor.
   * - ``M``
     - 20
     - body, arms, and head index groups
     - Non-mobility model descriptor.
   * - ``UB``
     - 14
     - upper-body index groups
     - Upper-body-only model descriptor.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::y1_model::A
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::y1_model::M
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::y1_model::UB
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`dyn-robot`
- :doc:`../state/robot-state`

.. rubric:: Examples

- ``get_robot_state.cpp`` and ``demo_motion.cpp`` both depend on one of these
  descriptors at compile time.
