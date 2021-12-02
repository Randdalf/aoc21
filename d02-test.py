#!/usr/bin/env python

"""Advent of Code 2021, Day 2 (Unit Tests)"""

import unittest

from d02 import parse, plot_course

example1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class PlotCourseTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(plot_course(parse(example1)), 150)


if __name__ == "__main__":
    unittest.main()
