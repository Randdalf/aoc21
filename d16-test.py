#!/usr/bin/env python

"""Advent of Code 2021, Day 16 (Unit Tests)"""

import unittest

from d16 import parse, version_sum, evaluate

example1 = "D2FE28"
example2 = "38006F45291200"
example3 = "EE00D40C823060"
example4 = "8A004A801A8002F478"
example5 = "620080001611562C8802118E34"
example6 = "C0015000016115A2E0802F182340"
example7 = "A0016C880162017C3686B18A3D4780"

example8 = "C200B40A82"
example9 = "04005AC33890"
example10 = "880086C3E88112"
example11 = "CE00C43D881120"
example12 = "D8005AC2A8F0"
example13 = "F600BC2D8F"
example14 = "9C005AC2F8F0"
example15 = "9C0141080250320F1802104A08"


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


class EvaluateTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(evaluate(parse(example1)), 2021)

    def test_example8(slf):
        slf.assertEqual(evaluate(parse(example8)), 3)

    def test_example9(slf):
        slf.assertEqual(evaluate(parse(example9)), 54)

    def test_example10(slf):
        slf.assertEqual(evaluate(parse(example10)), 7)

    def test_example11(slf):
        slf.assertEqual(evaluate(parse(example11)), 9)

    def test_example12(slf):
        slf.assertEqual(evaluate(parse(example12)), 1)

    def test_example13(slf):
        slf.assertEqual(evaluate(parse(example13)), 0)

    def test_example14(slf):
        slf.assertEqual(evaluate(parse(example14)), 0)

    def test_example15(slf):
        slf.assertEqual(evaluate(parse(example15)), 1)


if __name__ == "__main__":
    unittest.main()
