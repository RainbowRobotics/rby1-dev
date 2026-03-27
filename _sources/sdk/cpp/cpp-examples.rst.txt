C++ Examples
============

The vendored SDK ships C++ examples under ``external/rby1-sdk/examples/cpp``.
Use this page to pick a runnable starting point, then jump back into the
class-reference pages for the specific types that appear in the sample.

.. rubric:: Recommended First Files

- ``get_robot_state.cpp`` for the smallest client-side state example.
- ``demo_motion.cpp`` for the standard power, servo, control-manager, and
  command flow.
- ``real_time_control_command.cpp`` for the advanced UDP control callback path.
- ``dynamics/load_urdf.cpp`` for a pure model-and-dynamics entry point.

.. rubric:: Connection & State

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Example
     - Main types
     - What it demonstrates
   * - ``get_robot_state.cpp``
     - ``rb::Robot``, ``rb::RobotState``
     - Connect, start state updates, and inspect live measurements.
   * - ``get_robot_state2.cpp``
     - ``rb::Robot``, ``rb::RobotState``
     - Alternate state polling and monitoring flow.
   * - ``log.cpp``
     - ``rb::Robot``, ``rb::Log``
     - Read recent logs and stream new log records.

.. rubric:: Motion & Commands

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Example
     - Main types
     - What it demonstrates
   * - ``demo_motion.cpp``
     - ``rb::Robot``, command builders
     - Standard command submission from the high-level client.
   * - ``stop_command.cpp``
     - ``rb::StopCommandBuilder``
     - Stop-command submission through the whole-body builder path.
   * - ``power_command.cpp``
     - ``rb::Robot``
     - Power control through the robot client.
   * - ``mobility_command.cpp``
     - ``rb::MobilityCommandBuilder``, ``rb::SE2VelocityCommandBuilder``
     - Mobility and planar-base command composition.
   * - ``reset_odometry.cpp``
     - ``rb::Robot``
     - Odometry reset from the client API.

.. rubric:: Real-Time & Control

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Example
     - Main types
     - What it demonstrates
   * - ``real_time_control_command.cpp``
     - ``rb::ControlInput``, ``rb::ControlState``, ``rb::Robot``
     - Real-time control callback with model-based computation.
   * - ``optimal_control.cpp``
     - ``rb::OptimalControlCommandBuilder``, ``rb::OptimalControl``
     - Optimal-control command and solver usage.
   * - ``gravity_compensation.cpp``
     - ``rb::GravityCompensationCommandBuilder``
     - Gravity compensation command composition.
   * - ``teleoperation_with_joint_mapping.cpp``
     - robot client, mapping utilities, master-arm flow
     - Joint-space teleoperation concepts.

.. rubric:: Dynamics & Math

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Example
     - Main types
     - What it demonstrates
   * - ``dynamics/load_urdf.cpp``
     - ``rb::dyn::Robot``, ``rb::dyn::State``
     - Load a URDF model and inspect the rigid-body tree.
   * - ``dynamics/dynamics_coeff.cpp``
     - ``rb::dyn::Robot``
     - Dynamic-coefficient calculations.
   * - ``dynamics/gravity_term.cpp``
     - ``rb::dyn::Robot``
     - Gravity term computation.
   * - ``dynamics/inverse_dynamics.cpp``
     - ``rb::dyn::Robot``
     - Inverse-dynamics computation.
   * - ``dynamics/mass_matrix.cpp``
     - ``rb::dyn::Robot``
     - Mass-matrix computation.
   * - ``dynamics/reflective_mass.cpp``
     - ``rb::dyn::Robot``
     - Reflective mass analysis.
   * - ``so3.cpp``
     - ``rb::math::SO3``
     - Rotation construction and conversion helpers.
   * - ``trapezoidal_motion_generator.cpp``
     - ``rb::TrapezoidalMotionGenerator``
     - Motion-profile generation.
   * - ``velocity_estimation.cpp``
     - ``rb::VelocityFilterEstimator``
     - Filter-based velocity estimation.

.. rubric:: Diagnostics & Modules

.. list-table::
   :header-rows: 1
   :widths: 28 28 44

   * - Example
     - Main types
     - What it demonstrates
   * - ``break_test.cpp``
     - ``rb::Robot``
     - Brake engagement and release flow.
   * - ``rtcomm_protocol.cpp``
     - UDP and protocol helpers
     - Lower-level RT communication inspection.
   * - ``kinematic_calibration.cpp`` and ``kinematic_calibration2.cpp``
     - robot client and model utilities
     - Calibration-oriented workflows.
   * - ``module_test/*``
     - ``rb::upc::MasterArm``, ``rb::DynamixelBus``, robot client
     - Module-level tests for gripper, torso, head, arms, tool flange, and
       master arm.
