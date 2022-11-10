#
# This file is part of snmpclitools software.
#
# Copyright (c) 2005-2019, Ilya Etingof <etingof@gmail.com>
# License: https://www.pysnmp.com/snmpclitools/license.html
#
from pysnmp import error


class SnmpApplicationError(error.PySnmpError):
    pass
