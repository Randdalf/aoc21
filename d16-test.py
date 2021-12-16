#!/usr/bin/env python

"""Advent of Code 2021, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, version_sum

example1 = "D2FE28"
example2 = "38006F45291200"
example3 = "EE00D40C823060"
example4 = "8A004A801A8002F478"
example5 = "620080001611562C8802118E34"
example6 = "C0015000016115A2E0802F182340"
example7 = "A0016C880162017C3686B18A3D4780"


class VersionSumTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(version_sum(parse(example1)), 6)

    def test_example2(slf):
        slf.assertEqual(version_sum(parse(example2)), 9)

    def test_example3(slf):
        slf.assertEqual(version_sum(parse(example3)), 14)

    def test_example4(slf):
        slf.assertEqual(version_sum(parse(example4)), 16)

    def test_example5(slf):
        slf.assertEqual(version_sum(parse(example5)), 12)

    def test_example6(slf):
        slf.assertEqual(version_sum(parse(example6)), 23)

    def test_example7(slf):
        slf.assertEqual(version_sum(parse(example7)), 31)


if __name__ == "__main__":
    unittest.main()
