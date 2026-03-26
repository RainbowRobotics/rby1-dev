RobotState
==========

``rb::RobotState<T>`` is the live state snapshot delivered through
``StartStateUpdate()`` or returned by ``GetState()``. The page also covers the
smaller state records that appear inside the top-level snapshot.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_state.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``struct`` family
   * - Primary role
     - Represent the live measured state of the robot and its peripherals.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Field group
     - Meaning
     - Notes
   * - ``system_stat``, ``battery_state``
     - Host-level and battery-related status.
     - Useful during bring-up and power diagnosis.
   * - ``power_states``, ``emo_states``, ``joint_states``
     - Per-device and per-joint subsystem state.
     - These are the main discrete device-status records.
   * - ``tool_flange_left``, ``tool_flange_right``
     - Tool-flange I/O and status.
     - Present for both end-effectors.
   * - ``ft_sensor_left``, ``ft_sensor_right``
     - Force-torque sensor data.
     - Includes freshness information in nested timestamp helpers.
   * - ``position``, ``velocity``, ``current``, ``temperature``
     - Main measured vectors.
     - Aligned with the robot model's joint ordering.
   * - ``target_position``, ``target_velocity``,
       ``target_feedback_gain``, ``target_feedforward_torque``
     - Command targets tracked by the control loop.
     - Useful when comparing request and measured output.
   * - ``center_of_mass``, ``gravity``, ``odometry``, ``collisions``
     - Higher-level computed state and environment-related outputs.
     - Often consumed by monitoring and model-based code.
   * - ``is_ready``
     - Readiness flag for command execution.
     - Use alongside :doc:`control-manager-state`.

.. rubric:: Units & Ranges

.. list-table::
   :header-rows: 1
   :widths: 34 18 48

   * - Field
     - Unit / encoding
     - Notes
   * - ``RobotState::timestamp``
     - Absolute timestamp
     - Captured as ``timespec`` in C++; Python bindings expose a wall-clock
       time point.
   * - ``SystemStat::cpu_usage``, ``SystemStat::memory_usage``
     - ``%``
     - Host resource usage percentages.
   * - ``SystemStat::uptime``, ``SystemStat::program_uptime``
     - ``s``
     - Elapsed uptime counters.
   * - ``BatteryState::voltage``, ``current``, ``level_percent``
     - ``V``, ``A``, ``%``
     - Battery pack measurements and charge estimate.
   * - ``PowerState::voltage``
     - ``V``
     - Supply voltage for one power-controlled device.
   * - ``JointState::time_since_last_update``,
       ``ToolFlangeState::time_since_last_update``,
       ``FTSensorData::time_since_last_update``
     - Elapsed time
     - Freshness durations stored as ``timespec``.
   * - ``JointState::position``, ``target_position``,
       ``RobotState::position``, ``target_position``
     - ``rad``
     - Joint-space positions in model order.
   * - ``JointState::velocity``, ``target_velocity``,
       ``RobotState::velocity``, ``target_velocity``
     - ``rad/s``
     - Joint-space velocity values in model order.
   * - ``JointState::current``, ``RobotState::current``
     - ``A``
     - Joint motor currents.
   * - ``JointState::torque``, ``target_feedforward_torque``,
       ``RobotState::torque``, ``target_feedforward_torque``, ``gravity``
     - ``Nm``
     - Measured torque, feedforward torque, and gravity term are all reported
       in joint torque units.
   * - ``JointState::target_feedback_gain``,
       ``RobotState::target_feedback_gain``
     - Dimensionless
     - Public headers document the per-joint target gain range as ``[0, 10]``.
   * - ``JointState::temperature``, ``RobotState::temperature``
     - ``deg C``
     - Joint temperatures are stored as integers.
   * - ``ToolFlangeState::gyro``, ``acceleration``,
       ``output_voltage``
     - ``rad/s``, ``m/s^2``, ``V``
     - End-effector IMU and output-rail measurements.
   * - ``FTSensorData::force``, ``torque``
     - ``N``, ``Nm``
     - Three-axis force and torque vectors.
   * - ``RobotState::odometry``
     - ``SE(2)``
     - Homogeneous planar pose. Translation terms are in meters and heading is
       encoded in the rotation block.
   * - ``RobotState::center_of_mass``
     - ``m``
     - Center-of-mass position expressed in the base frame.
   * - ``RobotState::collisions``
     - ``m``
     - ``CollisionResult::position1``, ``position2``, and ``distance`` are all
       in meters. Signed distance becomes negative on penetration.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::RobotState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::SystemStat
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::BatteryState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::PowerState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::EMOState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::JointState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::ToolFlangeState
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::FTSensorData
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`control-manager-state`
- :doc:`../models/model-descriptors`

.. rubric:: Examples

- ``get_robot_state.cpp`` and ``get_robot_state2.cpp`` are the most direct
  examples for this page.
