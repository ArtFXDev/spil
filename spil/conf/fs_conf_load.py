# -*- coding: utf-8 -*-
"""

This file is part of SPIL, The Simple Pipeline Lib.

(C) copyright 2019-2021 Michael Haussmann, spil@xeo.info

SPIL is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

SPIL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with SPIL.
If not, see <https://www.gnu.org/licenses/>.

"""
import importlib
import inspect

from spil.conf.util import pattern_replacing

# stubs that are replaced by imports
path_templates = {}
key_types = {}
key_patterns = {}
search_path_mapping = {}
sidkeys_to_extrakeys = {}
extrakeys_to_sidkeys = {}
path_mapping = {}
path_templates_reference = ''
path_defaults = {}

module = importlib.import_module('fs_conf')

__all__ = []
for name, value in inspect.getmembers(module):
    if name.startswith('__'):
        continue

    globals()[name] = value
    __all__.append(name)

pattern_replacing(path_templates, key_patterns)

if __name__ == '__main__':
    from pprint import pprint

    pprint(globals())
