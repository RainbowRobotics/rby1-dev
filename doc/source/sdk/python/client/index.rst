Robot
=====

.. currentmodule:: rby1_sdk

This section groups the primary robot entry points and model-specific classes.
Use it when you need to connect to a robot, fetch state, or work with a
particular model variant.

Each robot model has different degrees of freedom and basic structures,
so separate classes are provided for each model. For more information about
the models, see `Models <../../models/index.md>`_.

For each model, the table lists the model descriptor (``Model_*``), the robot
client (``Robot_*``), its command handlers, the real-time control types used by
``Robot_*.control()`` (``Robot_*_ControlState``, ``Robot_*_ControlInput``), and
the state snapshot (``RobotState_*``). The types inside a state snapshot are
listed on the State & Metadata page of this reference.

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   create_robot
   create_robot_a
   create_robot_m
   create_robot_ub

Robot A
~~~~~~~

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   Model_A
   Robot_A
   Robot_A_CommandHandler
   Robot_A_CommandStreamHandler
   Robot_A_ControlState
   Robot_A_ControlInput
   RobotState_A

Robot M
~~~~~~~

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   Model_M
   Robot_M
   Robot_M_CommandHandler
   Robot_M_CommandStreamHandler
   Robot_M_ControlState
   Robot_M_ControlInput
   RobotState_M

Robot UB
~~~~~~~~

.. autosummary::
   :toctree: ../generated
   :nosignatures:

   Model_UB
   Robot_UB
   Robot_UB_CommandHandler
   Robot_UB_CommandStreamHandler
   Robot_UB_ControlState
   Robot_UB_ControlInput
   RobotState_UB

.. rubric:: Real-time control

``Robot_*.control(callback)`` runs a real-time loop and calls ``callback(state)``
every control cycle until the callback returns an input with ``finish = True``.
The callback gets a ``Robot_*_ControlState`` and returns a
``Robot_*_ControlInput`` of the same model. ``mode`` is a boolean array:
``False`` means ``target`` is a position in ``rad``, ``True`` means ``target``
is a velocity in ``rad/s``. The C++ page
`ControlInput & ControlState <../../cpp/client/control-loop-types.md>`_
describes the fields in detail.

The snippet below is shortened from ``examples/python/34_real_time_control.py``.
On the first cycle it stores the measured position and returns it as the
target, so the robot holds its current pose.

.. code-block:: python

   import rby1_sdk as rby

   held = {"q": None}

   def control_fn(state: rby.Robot_A_ControlState):
       if held["q"] is None:
           held["q"] = state.position.copy()  # Hold the current pose.
       i = rby.Robot_A_ControlInput()        # mode = False (position) for every joint
       i.target = held["q"]
       i.feedback_gain.fill(10)
       i.feedforward_torque.fill(0)
       i.finish = False                      # Return True to end control().
       return i

   ok = robot.control(control_fn)  # Blocks until finish is True or the loop fails.

.. warning::

   The example in the ``control()`` docstring of v0.10.1 does not run as
   written: ``ControlInput`` and ``rby.ControlMode`` do not exist (use
   ``rby.Robot_A_ControlInput`` and so on). It also sets ``target`` to zeros,
   which moves every joint to the zero pose from the first cycle instead of
   holding the current pose. Real-time control moves the robot every cycle with the targets you
   return. Clear the area around the robot and keep the E-Stop within reach.
