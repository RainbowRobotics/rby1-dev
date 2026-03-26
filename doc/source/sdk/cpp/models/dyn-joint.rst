dyn::Joint
==========

``rb::dyn::Joint`` represents one joint in the rigid-body model tree. It
provides factories for fixed, prismatic, and revolute joints and exposes the
limit metadata that model-based code often needs.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/dynamics/joint.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::dyn``
   * - Kind
     - ``class``
   * - Primary role
     - Represent one joint and its connectivity, motion subspace, and limits.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Make(...)``, ``MakeFixedJoint(...)``, ``MakePrismaticJoint(...)``,
       ``MakeRevoluteJoint(...)``
     - Construct new joint objects.
     - Static factories for the main joint families.
   * - ``ConnectLinks(...)`` and ``Disconnect()``
     - Attach or detach parent and child links.
     - Use while building or editing a model.
   * - ``GetParentLink()``, ``GetChildLink()``, ``GetName()``, ``IsFixed()``
     - Inspect identity and connectivity.
     - Useful during model traversal.
   * - ``GetLimit*()`` and ``SetLimit*()``
     - Read or write joint, velocity, acceleration, and torque limits.
     - Important for controllers and safety checks.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::dyn::Joint
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dyn-link`
- :doc:`dyn-robot`

.. rubric:: Examples

- ``dynamics/load_urdf.cpp`` and ``dynamics/simple_robot.cpp`` are the most
  relevant entry points.
