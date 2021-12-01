#!/usr/bin/env python

"""Advent of Code 2021, Day 1 (Unit Tests)"""

import unittest

from d01 import parse, increases

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


class IncreasesTests(unittest.TestCase):
    def test_example1_1(slf):
        slf.assertEqual(increases(parse(example1), 1), 7)

    def test_example1_3(slf):
        slf.assertEqual(increases(parse(example1), 3), 5)


if __name__ == "__main__":
    unittest.main()
