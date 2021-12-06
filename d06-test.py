#!/usr/bin/env python

"""Advent of Code 2021, Day 6 (Unit Tests)"""

import unittest

from d06 import parse, simulate

example1 = "3,4,3,1,2"


class SimulateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(simulate(parse(example1)), 5934)


if __name__ == "__main__":
    unittest.main()
