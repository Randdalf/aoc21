#!/usr/bin/env python

"""Advent of Code 2021, Day 9"""

from aoc import solve


class Heightmap:
    def __init__(slf, data):
        slf.cells = [[int(x) for x in row] for row in data.split('\n')]
        slf.w = len(slf.cells[0])
        slf.h = len(slf.cells)

    def get(slf, x, y):
        return slf.cells[y][x]

    def neighbors(slf, x, y):
        if x > 0:
            yield slf.get(x-1, y)
        if y > 0:
            yield slf.get(x, y-1)
        if x < slf.w - 1:
            yield slf.get(x+1, y)
        if y < slf.h - 1:
            yield slf.get(x, y+1)


def parse(data):
    return Heightmap(data)


def risk_level(heightmap):
    total = 0
    for y in range(heightmap.h):
        for x in range(heightmap.w):
            height = heightmap.get(x, y)
            if all(height < n for n in heightmap.neighbors(x, y)):
                total += height + 1
    return total


if __name__ == "__main__":
    solve(9, parse, risk_level)
