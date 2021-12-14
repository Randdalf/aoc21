#!/usr/bin/env python

"""Advent of Code 2021, Day 14 (Unit Tests)"""

import unittest

from d14 import parse, common_elements

example1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""


class CommonElements10Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(common_elements(parse(example1), 10), 1588)


class CommonElements40Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(common_elements(parse(example1), 40), 2188189693529)


if __name__ == "__main__":
    unittest.main()
