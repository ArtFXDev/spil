# -*- coding: utf-8 -*-
"""
This file is part of SPIL, The Simple Pipeline Lib.

(C) copyright 2019-2022 Michael Haussmann, spil@xeo.info

SPIL is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

SPIL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with SPIL.
If not, see <https://www.gnu.org/licenses/>.

"""
"""
To launch searches on a custom data source.

 
Searches is a dict with searches as 
    key: search sid
    value: search description 

function: test_custom(searches) 
"""
import six
from spil_tests import Timer
from spil_tests.utils.test_utils import test_sid
from spil.util.log import DEBUG, ERROR, get_logger
from spil import Data, Sid

log = get_logger("spil_tests")
log.setLevel(DEBUG)


def test_custom(searches, data_source, as_sid=True, do_log=True, do_deep=False, do_doublon_check=True, do_match_check=False, replace=None):
    """
    Runs given searches on the given Data Source.

    Optionally operates a replace in the search, using given replace tuple.
    """

    global_timer = Timer(name="global", logger=log.debug)
    global_timer.start()

    for search_sid, comment in six.iteritems(searches):

        if replace:
            search_sid = search_sid.replace(*replace)

        log.debug("*" * 10)
        log.info("{} --> {} (source: {})".format(search_sid, comment, data_source))
        double_check = set()

        ls_timer = Timer(name="search_sid", logger=log.debug)
        ls_timer.start()
        count = 0
        for i in data_source.get(search_sid, as_sid=as_sid):
            if do_log:
                log.info(i)
            if do_match_check:
                match = Sid(i).match(search_sid)
                if not match:
                    log.warning('No match "{}" <-> "{}". This is not normal'.format(i, search_sid))
            count += 1
            if do_doublon_check:
                if i in double_check:
                    log.warning("--------------------------------------> Doublon {}".format(i))
                double_check.add(i)
            if do_deep:
                log.debug("Sid test for {}".format(i))
                test_sid(i, from_search=search_sid)

        log.debug("Total: " + str(count))
        ls_timer.stop()

    global_timer.stop()


if __name__ == "__main__":

    from spil.util.log import setLevel, ERROR, DEBUG

    setLevel(ERROR)

    searches = {}
    searches["FTOT/S/SQ0001/SH0010/*"] = ""

    test_custom(searches, Data())