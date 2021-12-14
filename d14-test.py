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


class CommonElementsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(common_elements(parse(example1)), 1588)


if __name__ == "__main__":
    unittest.main()
