SerialStream
============

``rb::SerialStream`` is a connection to a serial device on the robot PC (RPC),
opened through the robot client with ``Robot::OpenSerialStream()``. Use it for
asynchronous serial I/O with a device attached to the robot.
``Robot::GetSerialDeviceList()`` returns the available devices as
``rb::SerialDevice`` records (``path``, ``description``).

The SDK serial examples (``38_serial_device.cpp``, ``39_serial_communication.cpp``)
note that they do not run in simulation and do not apply while the Control
Manager is enabled. A device that sends data as soon as it connects, such as
some sensors, can overload the RPC.

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

.. rubric:: SerialDevice

.. doxygenstruct:: rb::SerialDevice
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`robot`
- :doc:`../utilities/dynamixel-bus`

.. rubric:: Examples

- `38_serial_device.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/38_serial_device.cpp>`__: lists serial devices with ``GetSerialDeviceList()``.
- `39_serial_communication.cpp <https://github.com/RainbowRobotics/rby1-sdk/blob/v0.10.1/examples/cpp/39_serial_communication.cpp>`__: opens a ``SerialStream``, sets a read callback and writes data.

All files are in ``examples/cpp`` of rby1-sdk v0.10.1. See :doc:`../cpp-examples` for the full list.
