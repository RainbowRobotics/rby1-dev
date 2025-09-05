C++ API Reference
=================

.. This section uses **Breathe** to render Doxygen XML.

.. Build Doxygen XML
.. -----------------

.. Example Doxyfile excerpt:

.. .. code-block:: make

..    PROJECT_NAME           = "rby1_cpp"
..    GENERATE_XML           = YES
..    XML_OUTPUT             = xml
..    RECURSIVE              = YES
..    QUIET                  = YES
..    EXTRACT_ALL            = YES
..    EXTRACT_STATIC         = YES
..    EXTRACT_PRIVATE        = NO
..    WARN_IF_UNDOCUMENTED   = NO

.. Run:

.. .. code-block:: bash

..    doxygen Doxyfile
..    # Ensure conf.py's breathe_projects["rby1_cpp"] points to the XML dir,
..    # e.g. export DOXYGEN_XML=/path/to/xml

.. Examples
.. --------

.. .. note::
..    Replace class/namespace names below with your actual API.

.. .. doxygennamespace:: rb
..    :content-only:
..    :members:

.. .. doxygenclass:: rb::Robot
..    :project: rby1_cpp
..    :members:
..    :protected-members:
..    :undoc-members:
