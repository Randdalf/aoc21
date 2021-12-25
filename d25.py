#!/usr/bin/env python

"""Advent of Code 2021, Day 25"""

from aoc import solve
from vec2 import Vec2


class State:
    def __init__(slf, east, south, w, h):
        slf.east = east
        slf.south = south
        slf.w = w
        slf.h = h

    def step(slf):
        moved = 0

        new_east = set()
        for pos in slf.east:
            adj = Vec2((pos.x + 1) % slf.w, pos.y)
            if adj in slf.east or adj in slf.south:
                new_east.add(pos)
            else:
                new_east.add(adj)
                moved += 1
        slf.east = new_east

        new_south = set()
        for pos in slf.south:
            adj = Vec2(pos.x, (pos.y + 1) % slf.h)
            if adj in slf.east or adj in slf.south:
                new_south.add(pos)
            else:
                new_south.add(adj)
                moved += 1
        slf.south = new_south

        return moved


def parse(data):
    east = set()
    south = set()
    rows = data.split('\n')
    h = len(rows)
    for y, row in enumerate(rows):
        w = len(row)
        for x, cell in enumerate(row):
            if cell == '>':
                east.add(Vec2(x, y))
            elif cell == 'v':
                south.add(Vec2(x, y))
    return State(east, south, w, h)


def sea_cucumbers(state):
    steps = 1
    while state.step() > 0:
        steps += 1
    return steps


if __name__ == "__main__":
    solve(25, parse, sea_cucumbers)
