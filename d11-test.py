#!/usr/bin/env python

"""Advent of Code 2021, Day 11 (Unit Tests)"""

import unittest

from d11 import parse, flashes, simul

example1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""


class FlashesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(flashes(parse(example1)), 1656)


class SimulTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(simul(parse(example1)), 195)


if __name__ == "__main__":
    unittest.main()
