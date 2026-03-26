SerialStream
============

``rb::SerialStream`` exposes an SDK-managed serial-device connection. It sits
next to the main robot client and is useful when you need asynchronous serial
I/O through the same SDK surface.

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
     - ``class``
   * - Primary role
     - Open, monitor, and write to an SDK-managed serial stream.

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Method
     - Purpose
     - Notes
   * - ``Connect(...)`` and ``Disconnect()``
     - Open or close the serial stream.
     - ``Connect(...)`` optionally prints verbose diagnostics.
   * - ``IsOpened()``, ``IsDone()``, ``IsCancelled()``
     - Inspect the current state of the stream.
     - Useful when the stream is managed asynchronously.
   * - ``SetReadCallback(...)``
     - Register a callback for incoming serial data.
     - The callback receives decoded strings.
   * - ``Write(...)`` and ``WriteByte(...)``
     - Send bytes or strings to the device.
     - Overloads cover raw byte buffers and string payloads.
   * - ``Wait()`` and ``WaitFor(...)``
     - Block until the stream finishes.
     - ``WaitFor(...)`` is the timed variant.

.. rubric:: Numeric Parameters & Encodings

.. list-table::
   :header-rows: 1
   :widths: 30 22 48

   * - Method
     - Unit / encoding
     - Notes
   * - ``WaitFor(timeout_ms)``
     - ``ms``
     - Timeout for waiting on stream shutdown.
   * - ``WriteByte(...)``
     - Byte value
     - Raw serial byte payload, not an SDK-level physical unit.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::SerialStream
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot`
- :doc:`../utilities/dynamixel-bus`

.. rubric:: Examples

- ``module_test/*`` examples are the closest reference points when the workflow
  involves direct peripheral communication.
