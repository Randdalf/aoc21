#!/usr/bin/env python

"""Advent of Code 2021, Day 9"""

from functools import reduce
from operator import mul

from aoc import solve


class Heightmap:
    def __init__(slf, data):
        slf.heights = [[int(x) for x in row] for row in data.split('\n')]
        slf.w = len(slf.heights[0])
        slf.h = len(slf.heights)

    def get(slf, x, y):
        return x, y, slf.heights[y][x]

    def neighbors(slf, x, y):
        if x > 0:
            yield slf.get(x-1, y)
        if y > 0:
            yield slf.get(x, y-1)
        if x < slf.w - 1:
            yield slf.get(x+1, y)
        if y < slf.h - 1:
            yield slf.get(x, y+1)

    @property
    def low_points(slf):
        for y in range(slf.h):
            for x in range(slf.w):
                height = slf.get(x, y)[2]
                if all(height < n for x, y, n in slf.neighbors(x, y)):
                    yield x, y, height


def parse(data):
    return Heightmap(data)


def risk_level(heightmap):
    return sum(height + 1 for x, y, height in heightmap.low_points)


def largest_basins(heightmap):
    basins = []
    for low in heightmap.low_points:
        basin = set()
        open = {low}
        while len(open) > 0:
            x, y, height = open.pop()
            for neighbor in heightmap.neighbors(x, y):
                if neighbor[2] < 9 and neighbor[2] > height:
                    open.add(neighbor)
            basin.add((x, y, height))
        basins.append(len(basin))
    return reduce(mul, sorted(basins, reverse=True)[:3])


if __name__ == "__main__":
    solve(9, parse, risk_level, largest_basins)
