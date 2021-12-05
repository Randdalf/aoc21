#!/usr/bin/env python

"""Advent of Code 2021, Day 5 (Unit Tests)"""

import unittest

from d05 import parse, overlaps

example1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


class OverlapsTests(unittest.TestCase):
    def test_example1_1(slf):
        slf.assertEqual(overlaps(parse(example1), False), 5)

    def test_example1_2(slf):
        slf.assertEqual(overlaps(parse(example1), True), 12)


if __name__ == "__main__":
    unittest.main()
