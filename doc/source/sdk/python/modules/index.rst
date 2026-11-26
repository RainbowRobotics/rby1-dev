Modules
=======

.. currentmodule:: rby1_sdk

SDK submodules for trajectory generation, user PC (UPC) devices, and dynamics.

.. autosummary::
   :toctree: ../generated
   :recursive:
   :nosignatures:

   math
   upc
   dynamics

.. rubric:: math

In the Python SDK, ``rby1_sdk.math`` contains only
``TrapezoidalMotionGenerator`` (trapezoidal velocity profile trajectories).
The module docstring also mentions Lie group operations; those
(``SE3``, ``SO3``, ``SE2``) exist only in the C++ SDK (``rb::math``).

.. rubric:: upc

Helpers for devices on the user PC (UPC): the leader arm and the gripper.
The module also exports these device path constants:

.. list-table::
   :header-rows: 1
   :widths: 34 30 36

   * - Name
     - Value
     - Notes
   * - ``upc.LeaderArmDeviceName``
     - ``"/dev/rby1_leader_arm"``
     - Current leader arm device link.
   * - ``upc.LegacyLeaderArmDeviceName``
     - ``"/dev/rby1_master_arm"``
     - Device link of older udev rules. ``resolve_leader_arm_device_name()``
       falls back to it when the current link does not exist.
   * - ``upc.MasterArmDeviceName``
     - ``"/dev/rby1_leader_arm"``
     - Deprecated alias of ``LeaderArmDeviceName``.
   * - ``upc.GripperDeviceName``
     - ``"/dev/rby1_gripper"``
     - Gripper device link.

``upc.MasterArm`` is a deprecated alias of ``upc.LeaderArm`` (renamed in
v0.10.0), and ``resolve_master_arm_device_name()`` is a deprecated alias of
``resolve_leader_arm_device_name()``. Use the new names in new code.

.. rubric:: dynamics

The dynamics classes come in one generic version and one version per
degree-of-freedom count. They have the same methods; only the DOF differs.

.. list-table::
   :header-rows: 1
   :widths: 30 20 50

   * - Class
     - DOF
     - Returned by
   * - ``dynamics.Robot_24``, ``dynamics.State_24``
     - 24
     - ``Robot_A.get_dynamics()`` (Model A)
   * - ``dynamics.Robot_26``, ``dynamics.State_26``
     - 26
     - ``Robot_M.get_dynamics()`` (Model M)
   * - ``dynamics.Robot_18``, ``dynamics.State_18``
     - 18
     - ``Robot_UB.get_dynamics()`` (upper body)
   * - ``dynamics.Robot``, ``dynamics.State``
     - any
     - ``dynamics.Robot(load_robot_from_urdf(path, base_link_name))`` for
       your own URDF

Typical use, from ``examples/python/19_dynamics_robot.py``:

.. code-block:: python

   model = robot.model()
   dyn_robot = robot.get_dynamics()
   dyn_state = dyn_robot.make_state(["base", "ee_right"], model.robot_joint_names)
   dyn_state.set_gravity(np.array([0, 0, 0, 0, 0, -9.81]))
   dyn_state.set_q(q)
   dyn_state.set_qdot(np.zeros(model.robot_dof))
   dyn_state.set_qddot(np.zeros(model.robot_dof))
   dyn_robot.compute_forward_kinematics(dyn_state)
   dyn_robot.compute_diff_forward_kinematics(dyn_state)
   dyn_robot.compute_2nd_diff_forward_kinematics(dyn_state)
   dyn_robot.compute_inverse_dynamics(dyn_state)
   tau = dyn_state.get_tau()  # joint torques [Nm]

The generated ``dynamics`` page lists ``base``, ``link_names`` and
``joint_names`` as attributes of the ``Robot`` classes. In v0.10.1 they are
methods: use ``get_base()``, ``get_link_names()`` and ``get_joint_names()``.
