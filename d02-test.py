#!/usr/bin/env python

"""Advent of Code 2021, Day 2 (Unit Tests)"""

import unittest

from d02 import parse, plot_course, Sub1, Sub2

example1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


class PlotCourseTests(unittest.TestCase):
    def test_example1_1(slf):
        slf.assertEqual(plot_course(parse(example1), Sub1()), 150)

    def test_example1_2(slf):
        slf.assertEqual(plot_course(parse(example1), Sub2()), 900)


if __name__ == "__main__":
    unittest.main()
