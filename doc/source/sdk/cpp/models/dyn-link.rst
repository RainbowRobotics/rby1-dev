dyn::Link
=========

``rb::dyn::Link`` represents one rigid link in the model tree. It owns the link
name, its collision set, and the parent or child joint relationships that make
up the robot structure.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/dynamics/link.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb::dyn``
   * - Kind
     - ``class``
   * - Primary role
     - Represent one rigid-body link and its attached collision geometry.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method group
     - Purpose
     - Notes
   * - ``Make(...)``
     - Construct a link with a default or explicit inertial matrix.
     - Static factory for new trees.
   * - ``AddCollision(...)`` and ``GetCollisions()``
     - Attach or inspect collision objects.
     - Use while building or auditing a model.
   * - ``GetParentJoint()`` and ``GetChildJointList()``
     - Traverse link-to-joint connectivity.
     - Exposed in mutable and const forms.
   * - ``GetName()``
     - Read the link name.
     - Useful for debugging and search.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::dyn::Link
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`dyn-joint`
- :doc:`dyn-inertial`
- :doc:`dyn-robot`

.. rubric:: Examples

- ``dynamics/load_urdf.cpp`` shows the link tree in context.
