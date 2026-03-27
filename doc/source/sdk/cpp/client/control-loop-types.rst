ControlInput & ControlState
===========================

``rb::ControlInput<T>`` and ``rb::ControlState<T>`` are the data structs passed
through ``Robot::Control()``. ``ControlState<T>`` carries the current measured
state into the callback and ``ControlInput<T>`` carries the next control output
back to the robot.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``struct template`` family
   * - Primary role
     - Carry measured state into the real-time callback and the generated
       command output back out.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 44 28

   * - Struct
     - Main fields
     - Description
   * - ``rb::ControlState<T>``
     - ``t``, ``position``, ``velocity``, ``current``, ``torque``, ``is_ready``
     - Measured state snapshot passed into the real-time callback.
   * - ``rb::ControlInput<T>``
     - ``target``, ``feedback_gain``, ``feedforward_torque``, ``mode``, ``finish``
     - Outgoing control command returned from the callback.

.. rubric:: Units & Encodings

.. list-table::
   :header-rows: 1
   :widths: 34 18 48

   * - Field
     - Unit / encoding
     - Notes
   * - ``ControlState::t``
     - ``s``
     - Real-time callback timestamp.
   * - ``ControlState::position``
     - ``rad``
     - Measured joint positions in model order.
   * - ``ControlState::velocity``
     - ``rad/s``
     - Measured joint velocities in model order.
   * - ``ControlState::current``
     - ``A``
     - Measured joint currents.
   * - ``ControlState::torque``
     - ``Nm``
     - Measured joint torques.
   * - ``ControlInput::target``
     - ``rad``
     - Commanded joint targets returned from the callback.
   * - ``ControlInput::feedback_gain``
     - Dimensionless
     - Integer gain value per joint. The public C++ headers do not define a
       fixed range.
   * - ``ControlInput::feedforward_torque``
     - ``Nm``
     - Joint feedforward torque term.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::ControlState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::ControlInput
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot`
- :doc:`../models/dyn-robot`
- :doc:`../models/model-descriptors`

.. rubric:: Examples

- ``real_time_control_command.cpp`` is the canonical example for both structs.
