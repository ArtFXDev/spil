# -*- coding: utf-8 -*-
"""
This file is part of SPIL, The Simple Pipeline Lib.

(C) copyright 2019-2023 Michael Haussmann, spil@xeo.info

SPIL is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

SPIL is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with SPIL.
If not, see <https://www.gnu.org/licenses/>.
"""
from __future__ import annotations
from typing import Iterable, List, overload, Optional
from typing_extensions import Literal

from spil.sid.sid import Sid
from spil.sid.read.util import first
from spil.sid.read.tools import unfold_search


class Finder:
    """
    Interface for Sid Finder.

    Implements common public Sid Search methods "find", "find_one", and "exists"

    The search process is as follows:
        find():
        - the search sid string is "unfolded" into a list of typed search Sids.

        do_find()
        - runs the actual search on each typed search sid
    """

    def __init__(self):
        pass

    @overload
    def find(self, search_sid: str | Sid, as_sid: Literal[True]) -> Iterable[Sid]:
        ...

    @overload
    def find(self, search_sid: str | Sid, as_sid: Literal[False]) -> Iterable[str]:
        ...

    @overload
    def find(self, search_sid: str | Sid, as_sid: Optional[bool]) -> Iterable[Sid] | Iterable[str]:
        ...

    def find(self, search_sid: str | Sid, as_sid: Optional[bool] = True) -> Iterable[Sid] | Iterable[str]:
        """
        Yields the Sids found using the given search_sid.
        Returns a generator over Sids, if as_sid is True (default), or over Sid strings.

        Example:

            >>> for sid in Finder().find('hamlet/a/*'):
            >>>     print(f"Found: {sid}")
            Found: hamlet/a/char
            Found: hamlet/a/prop
            Found: hamlet/a/location
            Found: hamlet/a/fx

        Args:
            search_sid: typed or untyped Sid or string
            as_sid: if the result should be Sid objects or strings

        Returns:
            Generator over Sids or strings
        """
        # shortcut if Sid is not a search
        sid = Sid(search_sid)
        if sid and not sid.is_search():
            generator = self.do_find([sid], as_sid=as_sid)
        else:
            search_sids = unfold_search(search_sid)
            generator = self.do_find(search_sids, as_sid=as_sid)

        for i in generator:
            yield i

    def do_find(self, search_sids: List[Sid], as_sid: Optional[bool] = True) -> Iterable[Sid] | Iterable[str]:
        raise NotImplementedError(
            f"[Finder.do_find] is abstract, and seams not implemented. Class: {self.__class__}"
        )

    @overload
    def find_one(self, search_sid: str | Sid, as_sid: Literal[True]) -> Sid:
        ...

    @overload
    def find_one(self, search_sid: str | Sid, as_sid: Literal[False]) -> str:
        ...

    @overload
    def find_one(self, search_sid: str | Sid, as_sid: Optional[bool]) -> Sid | str:
        ...

    def find_one(self, search_sid: str | Sid, as_sid: Optional[bool] = True) -> Sid | str:
        """
        Returns the first Sid found using the given search_sid.

        Returns a Sid, if as_sid is True (default), or a Sid strings.

        Internally calls "first" on "find".

        Example:

            >>> Finder().find_one('hamlet/a/char/ophelia')
            Sid("hamlet/a/char/ophelia")

        Args:
            search_sid: typed or untyped Sid or string
            as_sid: if the result should be a Sid object or string

        Returns:
            first found Sid or string

        """
        found = first(self.find(search_sid, as_sid=False))  # read is faster if as_sid is False
        if as_sid:
            return Sid(found)
        else:
            return found

    def exists(self, search_sid: str | Sid) -> bool:
        """
        Returns True if the given search_sid returns a result.
        Else False.

        Internally calls "bool" on "find_one".

        Example:

            >>> Finder().exists('hamlet/a/char/ophelia')
            True

            >>> Finder().exists('hamlet/a/char/jimmy')
            False

        Args:
            search_sid: search_sid: typed or untyped Sid or string

        Returns:
            True if search_sid returns a result, else False
        """
        return bool(self.find_one(search_sid, as_sid=False))

    def __str__(self):
        return f"[spil.{self.__class__.__name__}]"


if __name__ == "__main__":
    print(Finder())
