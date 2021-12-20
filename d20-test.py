#!/usr/bin/env python

"""Advent of Code 2021, Day 20 (Unit Tests)"""

import unittest

from d20 import parse, lit_pixels


example1 = """..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###"""


class LitPixels2Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(lit_pixels(parse(example1), 2), 35)


class LitPixels50Tests(unittest.TestCase):
    def test_example1(slf):
        slf.assertEqual(lit_pixels(parse(example1), 50), 3351)


if __name__ == "__main__":
    unittest.main()
