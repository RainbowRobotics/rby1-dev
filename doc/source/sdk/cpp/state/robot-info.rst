RobotInfo
=========

``rb::RobotInfo`` is the static metadata snapshot returned by
``Robot::GetRobotInfo()``. It bundles robot-level metadata and several smaller
records that describe batteries, power devices, EMO channels, and joints.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_info.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``struct`` family
   * - Primary role
     - Provide static robot, joint, and device metadata for client code.

.. rubric:: Public Attributes

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Field or record
     - Meaning
     - Notes
   * - ``RobotInfo``
     - Robot model, version, SDK version, subsystem joint indices, and lists of
       device records.
     - This is the top-level record most code reads first.
   * - ``JointInfo``
     - Metadata for one joint.
     - Used inside ``RobotInfo::joint_infos``.
   * - ``PowerInfo``
     - Metadata for one power-controlled device.
     - Used inside ``RobotInfo::power_infos``.
   * - ``EMOInfo``
     - Metadata for one emergency-stop source.
     - Used inside ``RobotInfo::emo_infos``.
   * - ``BatteryInfo``
     - Battery metadata placeholder or future extension record.
     - Carried as part of top-level battery metadata.

.. rubric:: Numeric Fields & Encodings

.. list-table::
   :header-rows: 1
   :widths: 32 20 48

   * - Field
     - Unit / encoding
     - Notes
   * - ``RobotInfo::degree_of_freedom``
     - Joint count
     - Total number of actuated degrees of freedom.
   * - ``RobotInfo::mobility_joint_idx``, ``body_joint_idx``,
       ``head_joint_idx``, ``torso_joint_idx``,
       ``right_arm_joint_idx``, ``left_arm_joint_idx``
     - Joint indices
     - Model-order joint indices for each subsystem partition.

.. rubric:: Detailed Reference

.. doxygenstruct:: rb::RobotInfo
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::JointInfo
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::PowerInfo
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::EMOInfo
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenstruct:: rb::BatteryInfo
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/robot`
- :doc:`robot-state`
- :doc:`../models/model-descriptors`

.. rubric:: Examples

- ``get_robot_state.cpp`` and ``demo_motion.cpp`` are the right entry points
  when you want to compare static metadata with live state.
