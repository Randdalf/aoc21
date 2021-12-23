#!/usr/bin/env python

"""Advent of Code 2021, Day 23 (Unit Tests)"""

import unittest

from d23 import parse, least_energy

example1 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""


class LeastEnergyTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(least_energy(parse(example1)), 12521)


if __name__ == "__main__":
    unittest.main()
