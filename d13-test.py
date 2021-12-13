#!/usr/bin/env python

"""Advent of Code 2021, Day 13 (Unit Tests)"""

import unittest

from d13 import parse, count_dots

example1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5"""


class CountDotsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(count_dots(parse(example1)), 17)


if __name__ == "__main__":
    unittest.main()
