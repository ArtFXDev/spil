# -*- coding: utf-8 -*-
"""

This file is part of SPIL, The Simple Pipeline Lib.

(C) copyright 2019-2022 Michael Haussmann, spil@xeo.info

SPIL is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

SPIL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with SPIL.
If not, see <https://www.gnu.org/licenses/>.

"""
import traceback
from spil.conf.global_conf import __version__

try:
    from spil import conf  # default config bootstrap
    from spil.sid.sid import Sid

    from spil.sid.read.finder import Finder
    from spil.sid.read.finders.find_paths import FindInPaths
    from spil.sid.read.finders.find_list import FindInList
    from spil.sid.read.finders.find_constants import FindInConstants
    from spil.sid.read.finders.find_finders import FindInFinders

    from spil.sid.read.getter import Getter
    from spil.sid.write.writer import Writer

    from spil.util.exception import SpilException
    from spil.util import log
    from spil.util import log as logging  # to use as standard logging and create custom loggers
    from spil.util.log import setLevel, ERROR

    setLevel(ERROR)
except Exception as e:
    traceback.print_exc()
    raise Exception(
        "Spil is imported, but impossible to import spil packages. \n Please check compatibility of your sid_conf and fs_conf files."
    )
