#!/usr/bin/env python

"""Advent of Code 2021, Day 18 (Unit Tests)"""

import unittest

from d18 import parse, final_sum, largest_mag

example1 = """[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]"""


class FinalSumTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(final_sum(parse(example1)), 4140)


class LargestMagTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(largest_mag(parse(example1)), 3993)


if __name__ == "__main__":
    unittest.main()
