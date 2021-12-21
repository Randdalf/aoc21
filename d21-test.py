#!/usr/bin/env python

"""Advent of Code 2021, Day 21 (Unit Tests)"""

import unittest

from d21 import parse, dirac_dice

example1 = """Player 1 starting position: 4
Player 2 starting position: 8"""


class DiraceDiceTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(dirac_dice(parse(example1)), 739785)


if __name__ == "__main__":
    unittest.main()
