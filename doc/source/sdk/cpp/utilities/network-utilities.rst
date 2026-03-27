Network Utilities
=================

These transport classes expose the lower-level UDP layer used by the SDK's
real-time path. Most application code will stay at ``rb::Robot<T>``, but these
types are useful when you need direct transport control.

.. rubric:: Headers

.. list-table::
   :header-rows: 1
   :widths: 32 68

   * - Type
     - Header
   * - ``rb::UdpClient``
     - ``#include <rby1-sdk/net/udp_client.h>``
   * - ``rb::UdpIPv4Client`` and ``rb::UdpIPv6Client``
     - ``#include <rby1-sdk/net/udp_client.h>``
   * - ``rb::UdpServer``
     - ``#include <rby1-sdk/net/udp_server.h>``

.. rubric:: Public Member Functions

.. list-table::
   :header-rows: 1
   :widths: 28 48 24

   * - Type or method group
     - Purpose
     - Notes
   * - ``rb::UdpClient``
     - Base transport interface for ``SendTo(...)`` and ``RecvFrom(...)``.
     - Implemented by the IPv4 and IPv6 client classes.
   * - ``rb::UdpIPv4Client`` and ``rb::UdpIPv6Client``
     - Connect to a specific remote UDP endpoint and send or receive packets.
     - Choose the variant that matches the target address family.
   * - ``rb::UdpServer``
     - Bind a local UDP socket, receive packets, and reply to clients.
     - Useful for protocol tools and custom RT experiments.

.. rubric:: Detailed Reference

.. doxygenclass:: rb::UdpClient
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::UdpIPv4Client
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::UdpIPv6Client
   :project: rby1-sdk
   :members:
   :undoc-members:

.. doxygenclass:: rb::UdpServer
   :project: rby1-sdk
   :members:
   :undoc-members:

.. rubric:: Related Types

- :doc:`../client/control-loop-types`
- :doc:`threading-and-time-utilities`

.. rubric:: Examples

- ``real_time_control_command.cpp``
- ``rtcomm_protocol.cpp``
