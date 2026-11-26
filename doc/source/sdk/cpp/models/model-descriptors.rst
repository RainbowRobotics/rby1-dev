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
     - ``kMobilityIdx`` (2 wheels), ``kBodyIdx`` (20: torso 6, arms 7 + 7),
       ``kHeadIdx`` (2)
     - RB-Y1 Model A, mobile base with two wheels.
   * - ``M``
     - 26
     - ``kMobilityIdx`` (4 wheels), ``kBodyIdx`` (20: torso 6, arms 7 + 7),
       ``kHeadIdx`` (2)
     - RB-Y1 Model M, mobile base with four wheels. A separate class; it does
       not inherit from ``A``.
   * - ``UB``
     - 18
     - ``kMobilityIdx`` (empty), ``kBodyIdx`` (16: torso 2, arms 7 + 7),
       ``kHeadIdx`` (2)
     - RB-Y1 upper body without a mobile base.

All three classes also define ``kModelName``, ``kRobotJointNames``,
``kRightArmIdx``, ``kLeftArmIdx``, ``kTorsoIdx``, ``kControlPeriod``
(``0.002`` s) and the dynamics types ``DynRobotType`` / ``DynRobotStateType``.
All constants are ``static constexpr``, so they can be used as template
arguments (for example ``Eigen::Vector<double, rb::y1_model::A::kRobotDOF>``).

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

- `01_hello_rby1.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/01_hello_rby1.cpp>`__: selects ``y1_model::A`` or ``y1_model::M`` from the ``--model`` argument.
- `00_helper.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/00_helper.cpp>`__: helper templates that take the model descriptor as ``ModelT``.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
