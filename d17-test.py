#!/usr/bin/env python

"""Advent of Code 2021, Day 17 (Unit Tests)"""

import unittest

from d17 import parse, apex_y, initial_v

example1 = "target area: x=20..30, y=-10..-5"


class ApexYTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(apex_y(parse(example1)), 45)


class InitialVTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(initial_v(parse(example1)), 112)


if __name__ == "__main__":
    unittest.main()
