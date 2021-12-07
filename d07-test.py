#!/usr/bin/env python

"""Advent of Code 2021, Day 7 (Unit Tests)"""

import unittest

from d07 import parse, min_fuel

example1 = "16,1,2,0,4,2,7,1,2,14"


class MinFuelTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(min_fuel(parse(example1)), 37)


if __name__ == "__main__":
    unittest.main()
