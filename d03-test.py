#!/usr/bin/env python

"""Advent of Code 2021, Day 3 (Unit Tests)"""

import unittest

from d03 import parse, power_consumption

example1 = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


class PowerConsumptionTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(power_consumption(parse(example1)), 198)


if __name__ == "__main__":
    unittest.main()
