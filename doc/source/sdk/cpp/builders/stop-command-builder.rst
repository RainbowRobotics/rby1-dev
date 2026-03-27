StopCommandBuilder
==================

``rb::StopCommandBuilder`` is the explicit stop primitive. It carries no motion
payload beyond the shared command header.

.. rubric:: Header

.. list-table::
   :widths: 20 80

   * - Header
     - ``#include <rby1-sdk/robot_command_builder.h>``

.. rubric:: Declaration

.. list-table::
   :widths: 24 76

   * - Namespace
     - ``rb``
   * - Kind
     - ``class``
   * - Primary role
     - Represent an explicit stop request.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``SetCommandHeader(...)``
     - Attach shared header metadata.
     - This is the only configurable part of the stop primitive.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::StopCommandBuilder
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`whole-body-command-builder`

.. rubric:: Examples

- ``stop_command.cpp``
