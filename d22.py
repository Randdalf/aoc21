#!/usr/bin/env python

"""Advent of Code 2021, Day 22"""

import re

from aoc import solve


class Cuboid:
    def __init__(slf, low, high):
        slf.low = low
        slf.high = high

    def cubes(slf):
        for z in range(slf.low[2], 1 + slf.high[2]):
            for y in range(slf.low[1], 1 + slf.high[1]):
                for x in range(slf.low[0], 1 + slf.high[0]):
                    yield x, y, z

    def __repr__(slf):
        return f'{slf.low} -> {slf.high}'


def parse_cuboid(data):
    nums = [int(n) for axis in data.split(',') for n in axis[2:].split('..')]
    return Cuboid((nums[0], nums[2], nums[4]), (nums[1], nums[3], nums[5]))


def parse_step(data):
    switch, cuboid = data.split(' ')
    return switch == 'on', parse_cuboid(cuboid)


def parse(data):
    return [parse_step(line) for line in data.split('\n')]


def intersects(a, b):
    for axis in range(3):
        if a.low[axis] > b.high[axis] or b.low[axis] > a.high[axis]:
            return False
    return True


def init(steps):
    area = Cuboid((-50, -50, -50), (50, 50, 50))
    on = set()
    for switch, cuboid in steps:
        if not intersects(cuboid, area):
            continue
        if switch:
            on.update(cuboid.cubes())
        else:
            on.difference_update(cuboid.cubes())
    return len(on)


if __name__ == "__main__":
    solve(22, parse, init)
