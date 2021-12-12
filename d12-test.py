#!/usr/bin/env python

"""Advent of Code 2021, Day 12 (Unit Tests)"""

import unittest

from d12 import parse, passages

example1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""


class PassagesTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(passages(parse(example1)), 10)

    def test_example2(slf):
        slf.assertEqual(passages(parse(example2)), 19)

    def test_example3(slf):
        slf.assertEqual(passages(parse(example3)), 226)


if __name__ == "__main__":
    unittest.main()
