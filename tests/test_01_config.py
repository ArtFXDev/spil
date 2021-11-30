# -*- coding: utf-8 -*-
"""
This file is part of SPIL, The Simple Pipeline Lib.

(C) copyright 2019-2021 Michael Haussmann, spil@xeo.info

SPIL is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

SPIL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with SPIL.
If not, see <https://www.gnu.org/licenses/>.

"""
import six

from tests import test_00_init  # import needed before spil.conf

from spil.conf import sid_templates, path_templates

print(test_00_init)


def get_duplicates(items):
    unique = set()
    duplicate = set()
    for item in items:
        if item not in duplicate:
            unique.add(item)
        else:
            duplicate.add(item)
    return duplicate


def test_sid_duplicates():

    print('- Testing duplicates in sid_templates (sid_conf)...')

    duplicate_keys = get_duplicates(sid_templates.keys())
    if duplicate_keys:
        print('\tFAILED: Duplicate keys in sid_templates (sid_conf): {}'.format(duplicate_keys))
    else:
        print('\tOK: No duplicate in sid_template keys (sid_conf).')

    duplicate_values = get_duplicates(sid_templates.values())
    if duplicate_values:
        print('\tFAILED: Duplicate values in sid_templates (sid_conf): {}'.format(duplicate_values))
    else:
        print('\tOK: No duplicate in sid_templates values (sid_conf).')

    print()


def test_fs_duplicates():

    print('- Testing duplicates in path_templates (fs_conf)...')

    duplicate_keys = get_duplicates(path_templates.keys())
    if duplicate_keys:
        print('\tFAILED: Duplicate keys in path_templates (fs_conf): {}'.format(duplicate_keys))
    else:
        print('\tOK: No duplicate in path_templates keys (fs_conf).')

    duplicate_values = get_duplicates(path_templates.values())
    if duplicate_values:
        print('\tFAILED: Duplicate values in path_templates (fs_conf): {}'.format(duplicate_values))
    else:
        print('\tOK: No duplicate in path_templates values (fs_conf).')

    print()

def test_missing():

    print('- Testing missing in sid_conf vs fs_conf...')

    sid_keys = set(sid_templates.keys())
    fs_keys = set(path_templates.keys())

    to_ignore = {'project_root'}

    missing_in_fs_conf = sid_keys - fs_keys - to_ignore
    if missing_in_fs_conf:
        print('\tFAILED: Missing sid_conf keys in FS keys: {}'.format(missing_in_fs_conf))
    else:
        print('\tOK: all sid_conf keys are in FS keys.')

    missing_in_sid_conf = fs_keys - sid_keys - to_ignore
    if missing_in_sid_conf:
        print('\tFAILED: Missing FS keys in sid_conf keys: {}'.format(missing_in_sid_conf))
    else:
        print('\tOK: All FS keys are in sid_conf keys.')

    print()


if __name__ == '__main__':

    print()
    print('Sid Templates: ')
    for k, v in six.iteritems(sid_templates):
        print('{} -> {}'.format(k, v))

    print()
    print('Path Templates: ')
    for k, v in six.iteritems(path_templates):
        print('{} -> {}'.format(k, v))

    print()
    print('Tests:')
    test_sid_duplicates()
    test_fs_duplicates()
    test_missing()

    print('Done')
