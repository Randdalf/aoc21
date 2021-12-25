#!/usr/bin/env python

"""Advent of Code 2021, Day 25 (Unit Tests)"""

import unittest

from d25 import parse, sea_cucumbers

example1 = """v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>"""


class SeaCucumbersTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(sea_cucumbers(parse(example1)), 58)


if __name__ == "__main__":
    unittest.main()
