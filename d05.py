#!/usr/bin/env python

"""Advent of Code 2021, Day 5"""

from collections import Counter

from aoc import solve
from vec2 import Vec2


def parse_coord(data):
    return Vec2(*map(int, data.split(',')))


def parse_segment(data):
    return tuple(parse_coord(coord) for coord in data.split(' -> '))


def parse(data):
    return [parse_segment(line) for line in data.split('\n')]


def overlaps(lines):
    counter = Counter()
    for start, end in lines:
        if start.x == end.x:
            if start.y > end.y:
                counter.update(Vec2(start.x, y) for y in range(end.y, start.y+1))
            else:
                counter.update(Vec2(start.x, y) for y in range(start.y, end.y+1))
        elif start.y == end.y:
            if start.x > end.x:
                counter.update(Vec2(x, start.y) for x in range(end.x, start.x+1))
            else:
                counter.update(Vec2(x, start.y) for x in range(start.x, end.x+1))
    return sum(int(n > 1) for n in counter.values())


if __name__ == "__main__":
    solve(5, parse, overlaps)
