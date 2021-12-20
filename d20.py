#!/usr/bin/env python

"""Advent of Code 2021, Day 20"""

from collections import defaultdict

from aoc import solve


def parse(data):
    parts = data.split('\n\n')
    algorithm = [x == '#' for x in parts[0]]
    image = defaultdict(lambda: False)
    for y, row in enumerate(parts[1].split('\n')):
        for x, col in enumerate(row):
            image[(x, y)] = col == '#'
    return algorithm, image


def kernel(x, y):
    for oy in range(1, -2, -1):
        for ox in range(1, -2, -1):
            yield (x + ox, y + oy)


def enhance(algorithm, image, default):
    enhanced = defaultdict(lambda: default)
    for pos in {k for pos in image.keys() for k in kernel(*pos)}:
        index = sum(int(image[k]) << i for i, k in enumerate(kernel(*pos)))
        enhanced[pos] = algorithm[index]
    return enhanced


def lit_pixels(input, steps):
    algorithm, image = input
    for step in range(steps):
        image = enhance(algorithm, image, algorithm[0] and step % 2 == 0)
    return sum(int(x) for x in image.values())


if __name__ == "__main__":
    solve(20, parse, lambda x: lit_pixels(x, 2), lambda x: lit_pixels(x, 50))
