#!/usr/bin/env python

"""Advent of Code 2021, Day 20"""

from aoc import solve


def parse(data):
    parts = data.split('\n\n')
    algorithm = [x == '#' for x in parts[0]]
    image = set()
    for y, row in enumerate(parts[1].split('\n')):
        for x, col in enumerate(row):
            if col == '#':
                image.add((x, y))
    return algorithm, image


def kernel(x, y):
    yield (x + 1, y + 1)
    yield (x, y + 1)
    yield (x - 1, y + 1)
    yield (x + 1, y)
    yield (x, y)
    yield (x - 1, y)
    yield (x + 1, y - 1)
    yield (x, y - 1)
    yield (x - 1, y - 1)


def enhance(algorithm, image, p_in, p_out):
    enhanced = set()
    for pos in {k for pos in image for k in kernel(*pos)}:
        index = sum(int((k in image) == p_in) << i for i, k in enumerate(kernel(*pos)))
        if algorithm[index] == p_out:
            enhanced.add(pos)
    return enhanced


def lit_pixels(input, steps):
    algorithm, image = input
    finite = not algorithm[0]
    for step in range(steps):
        image = enhance(algorithm, image, finite or step % 2 == 0, finite or step % 2 == 1)
    return len(image)


if __name__ == "__main__":
    solve(20, parse, lambda x: lit_pixels(x, 2), lambda x: lit_pixels(x, 50))
