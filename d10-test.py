#!/usr/bin/env python

"""Advent of Code 2021, Day 10 (Unit Tests)"""

import unittest

from d10 import parse, syntax_errors

example1 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""


class SyntaxErrorsTests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(syntax_errors(parse(example1)), 26397)


if __name__ == "__main__":
    unittest.main()
