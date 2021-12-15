#!/usr/bin/env python

"""Advent of Code 2021, Day 15 (Unit Tests)"""

import unittest

from d15 import parse, lowest_risk

example1 = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class LowestRiskTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(lowest_risk(parse(example1)), 40)


if __name__ == "__main__":
    unittest.main()
