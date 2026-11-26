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
   * - ``ControlInput::mode``
     - ``bool`` per joint
     - ``false`` (``kPositionControlMode``): ``target`` is a position.
       ``true`` (``kVelocityControlMode``): ``target`` is a velocity, and the
       robot integrates it into the position target every control cycle.
       Both constants are in ``rb`` and defined in
       ``#include <rby1-sdk/net/real_time_control_protocol.h>``.
   * - ``ControlInput::target``
     - ``rad`` or ``rad/s``
     - Joint position target (``mode = false``) or joint velocity target
       (``mode = true``), in model order.
   * - ``ControlInput::feedback_gain``
     - Integer, ``0`` to ``10``
     - Position feedback gain per joint. The robot clamps values outside
       ``[0, 10]``. With ``0`` the joint has no position feedback and does not
       hold its position.
   * - ``ControlInput::finish``
     - ``bool``
     - Set to ``true`` to end ``Robot::Control()`` normally.
   * - ``ControlInput::feedforward_torque``
     - ``Nm``
     - Joint feedforward torque term.

.. rubric:: How the loop runs

- ``Robot::Control()`` is **blocking**. It runs a UDP real-time loop and calls
  your callback every control cycle until the callback returns
  ``finish = true`` (``Control()`` returns ``true``) or an error or abort ends
  the loop (``Control()`` returns ``false``).
- The value you return is applied to the motors in the next cycle. Keep the
  callback short and free of blocking calls and memory allocation.

.. warning::

   In velocity mode a ``target`` is in ``rad/s``. Sending a position in
   ``rad`` with ``mode = true`` makes the joint move continuously.
   A default-constructed ``ControlInput`` has ``target = 0``,
   ``feedback_gain = 0`` and ``mode = false`` for every joint, so it neither
   holds the current pose nor stays where the robot is. Fill every joint:
   on the first cycle, return the measured ``position`` as the position
   target with a non-zero ``feedback_gain`` (the example uses ``10``).

.. rubric:: Minimal Callback

Shortened from ``examples/cpp/34_real_time_control.cpp``. On the first cycle
the callback stores the measured position and returns it as the target, so the
robot holds its current pose. Change ``target`` from there in small steps (the
example uses ``TrapezoidalMotionGenerator``).

.. code-block:: cpp

   using namespace rb;
   using Model = y1_model::A;

   bool initialized = false;
   Eigen::Vector<double, Model::kRobotDOF> target;

   // Blocks until the callback returns finish = true or the loop fails.
   robot->Control([&](const ControlState<Model>& state) -> ControlInput<Model> {
     if (!initialized) {
       target = state.position;  // Hold the current pose.
       initialized = true;
     }
     ControlInput<Model> input;  // mode = false (position) for every joint
     input.target = target;
     input.feedback_gain.setConstant(10);
     input.feedforward_torque.setConstant(0);
     input.finish = false;  // Set to true to end Control().
     return input;
   });

The example runs ``Control()`` in its own thread and the robot must be
initialized first (power, servo, Control Manager), as in
``examples/cpp/00_helper.cpp``.

.. warning::

   Real-time control moves the robot every cycle with the targets you return.
   Clear the area around the robot and keep the E-Stop within reach.

.. note::

   The generated comment on ``ControlInput::target`` below says "Target
   positions for each joint [rad]". With ``mode = true`` the value is a
   velocity in ``rad/s``, as in the table above.

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

- `34_real_time_control.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/34_real_time_control.cpp>`__: the reference example for both structs.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
