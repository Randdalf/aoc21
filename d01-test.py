#!/usr/bin/env python

"""Advent of Code 2021, Day 1 (Unit Tests)"""

import unittest

from d01 import parse, depth_increases

example1 = """199
200
208
210
200
207
240
269
260
263"""


class DepthIncreasesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(depth_increases(parse(example1)), 7)


if __name__ == "__main__":
    unittest.main()
