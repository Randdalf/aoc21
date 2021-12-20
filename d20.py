#!/usr/bin/env python

"""Advent of Code 2021, Day 20"""

from collections import defaultdict

from aoc import solve
from vec2 import Vec2


def parse(data):
    parts = data.split('\n\n')
    algorithm = [x == '#' for x in parts[0]]
    image = defaultdict(lambda: False)
    for y, row in enumerate(parts[1].split('\n')):
        for x, col in enumerate(row):
            image[Vec2(x, y)] = col == '#'
    return algorithm, image


def kernel(pos):
    for oy in range(1, -2, -1):
        for ox in range(1, -2, -1):
            yield Vec2(pos.x + ox, pos.y + oy)


def enhance(algorithm, image, default):
    enhanced = defaultdict(lambda: default)
    for pos in {k for pos in image.keys() for k in kernel(pos)}:
        index = sum(int(image[k]) << i for i, k in enumerate(kernel(pos)))
        enhanced[pos] = algorithm[index]
    return enhanced


def lit_pixels(input, steps=2):
    algorithm, image = input
    for step in range(steps):
        image = enhance(algorithm, image, algorithm[0] and step % 2 == 0)
    return sum(int(x) for x in image.values())


if __name__ == "__main__":
    solve(20, parse, lit_pixels)
