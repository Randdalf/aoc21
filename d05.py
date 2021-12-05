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


def dir(x):
    return int(x > 0) - int(x < 0)


def traverse(start, end):
    offset = end - start
    step = Vec2(dir(offset.x), dir(offset.y))
    yield start
    while start != end:
        start += step
        yield start


def overlaps(lines, diags):
    counter = Counter()
    for start, end in lines:
        if not diags and start.x != end.x and start.y != end.y:
            continue
        counter.update(traverse(start, end))
    return sum(int(n > 1) for n in counter.values())


if __name__ == "__main__":
    solve(5, parse, lambda x: overlaps(x, False), lambda x: overlaps(x, True))
