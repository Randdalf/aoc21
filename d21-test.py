#!/usr/bin/env python

"""Advent of Code 2021, Day 21 (Unit Tests)"""

import unittest

from d21 import parse, practice_dirac_dice, real_dirac_dice

example1 = """Player 1 starting position: 4
Player 2 starting position: 8"""


class PracticeDiraceDiceTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(practice_dirac_dice(parse(example1)), 739785)


class RealDiraceDiceTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(real_dirac_dice(parse(example1)), 444356092776315)


if __name__ == "__main__":
    unittest.main()
