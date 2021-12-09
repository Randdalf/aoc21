#!/usr/bin/env python

"""Advent of Code 2021, Day 9 (Unit Tests)"""

import unittest

from d09 import parse, risk_level, largest_basins

example1 = """2199943210
3987894921
9856789892
8767896789
9899965678"""


class RiskLevelTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(risk_level(parse(example1)), 15)


class LargestBasinsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(largest_basins(parse(example1)), 1134)


if __name__ == "__main__":
    unittest.main()
