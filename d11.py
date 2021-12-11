#!/usr/bin/env python

"""Advent of Code 2021, Day 11"""

from itertools import product

from aoc import solve


def parse(data):
    return [[int(x) for x in row] for row in data.split('\n')]


def neighbors(y, x):
    if x > 0:
        yield y, x-1
    if y > 0:
        yield y-1, x
    if x < 9:
        yield y, x+1
    if y < 9:
        yield y+1, x
    if y > 0 and x > 0:
        yield y-1, x-1
    if y < 9 and x > 0:
        yield y+1, x-1
    if y > 0 and x < 9:
        yield y-1, x+1
    if y < 9 and x < 9:
        yield y+1, x+1


def flashes(grid, steps=100):
    total = 0
    for step in range(steps):
        ready = set()
        flashed = set()
        for y, x in product(range(10), range(10)):
            grid[y][x] += 1
            if grid[y][x] > 9:
                ready.add((y, x))
        while len(ready) > 0:
            octopus = ready.pop()
            for neighbor in neighbors(*octopus):
                if neighbor in flashed:
                    continue
                y, x = neighbor
                grid[y][x] += 1
                if grid[y][x] > 9:
                    ready.add(neighbor)
            flashed.add(octopus)
        for y, x in flashed:
            grid[y][x] = 0
        total += len(flashed)
    return total


if __name__ == "__main__":
    solve(11, parse, flashes)
