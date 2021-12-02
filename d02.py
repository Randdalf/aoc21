#!/usr/bin/env python

"""Advent of Code 2021, Day 2"""

from aoc import solve
from vec2 import Vec2

dirs = {
    'forward': Vec2(1, 0),
    'up': Vec2(0, -1),
    'down': Vec2(0, 1)
}


def parse(data):
    for line in data.split('\n'):
        a, b = line.split(' ')
        yield dirs[a] * int(b)


def plot_course(course):
    pos = sum(course, Vec2(0, 0))
    return pos.x * pos.y


if __name__ == "__main__":
    solve(2, parse, plot_course)
