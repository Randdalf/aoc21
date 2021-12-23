#!/usr/bin/env python

"""Advent of Code 2021, Day 23 (Unit Tests)"""

import unittest

from d23 import parse, least_energy

example1 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""


class LeastEnergyFoldedTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(least_energy(parse(example1), False), 12521)


class LeastEnergyUnfoldedTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(least_energy(parse(example1), True), 44169)


if __name__ == "__main__":
    unittest.main()
