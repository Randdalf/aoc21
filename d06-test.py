#!/usr/bin/env python

"""Advent of Code 2021, Day 6 (Unit Tests)"""

import unittest

from d06 import parse, simulate

example1 = "3,4,3,1,2"


class SimulateTests(unittest.TestCase):
    def test_example1_80(slf):
        slf.assertEqual(simulate(parse(example1), 80), 5934)

    def test_example1_256(slf):
        slf.assertEqual(simulate(parse(example1), 256), 26984457539)


if __name__ == "__main__":
    unittest.main()
