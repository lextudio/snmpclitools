
Getting SNMP tools
==================

.. toctree::
   :maxdepth: 2

The SNMP tools are provided under terms and conditions of BSD-style
license, and can be freely downloaded from 
`PyPI <https://pypi.org/project/snmpclitools-lextudio/>`_ or
GitHub (`master branch <https://github.com/lextudio/snmpclitools/archive/master.zip>`_).

The best way to obtain SNMP tools and dependencies is to *pip install*
them all into a Python virtual environment:

.. code-block:: bash

   $ python3 -m venv venv3
   $ . venv3/bin/activate
   $ pip install snmpclitools-lextudio

In case you are installing SNMP tools on an off-line system, the following
packages need to be downloaded and installed:

* `PyASN1 <https://pypi.org/project/pyasn1>`_,
  used for handling ASN.1 objects
* `PySNMP <https://pypi.org/project/pysnmp-lextudio>`_,
  SNMP engine implementation

Optional, but recommended:

* `PyCryptodomex <https://pypi.org/project/pycryptodomex>`_,
  used by SNMPv3 crypto features
* `PySMI <https://pypi.org/project/pysmi-lextudio>`_ for automatic
  MIB download and compilation. That helps visualizing more SNMP objects
* `Ply <https://pypi.org/project/ply/>`_, parser generator
  required by PySMI

In case of any issues, please open a `GitHub issue <https://github.com/lextudio/pysnmp/issues/new>`_ so
we could try to help out.
