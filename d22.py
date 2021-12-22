#!/usr/bin/env python

"""Advent of Code 2021, Day 22"""

from functools import reduce
from itertools import product
from operator import mul

from aoc import solve


class Cuboid:
    def __init__(slf, lo, hi):
        slf.lo = lo
        slf.hi = hi

    @property
    def volume(slf):
        return reduce(mul, (1 + h - l for l, h in zip(slf.lo, slf.hi)))

    def intersects(slf, otr):
        for axis in range(3):
            if slf.lo[axis] > otr.hi[axis] or otr.lo[axis] > slf.hi[axis]:
                return False
        return True

    def contains(slf, otr):
        return all(slf.lo[axis] <= otr.lo[axis] and slf.hi[axis] >= otr.hi[axis] for axis in range(3))

    def carve(slf, otr):
        overlap_lo = tuple(max(s, o) for s, o in zip(slf.lo, otr.lo))
        overlap_hi = tuple(min(s, o) for s, o in zip(slf.hi, otr.hi))
        edges = [
            otr.lo,
            overlap_lo,
            tuple(1 + x for x in overlap_hi),
            tuple(1 + x for x in otr.hi)
        ]
        for i, j, k in product(range(3), range(3), range(3)):
            if i == 1 and j == 1 and k == 1:
                continue
            lo = (edges[i][0], edges[j][1], edges[k][2])
            hi = (edges[i+1][0] - 1, edges[j+1][1] - 1, edges[k+1][2] - 1)
            if any(lo[axis] > hi[axis] for axis in range(3)):
                continue
            yield Cuboid(lo, hi)

    def __repr__(slf):
        return f'{slf.lo} -> {slf.hi}'


def parse_cuboid(data):
    nums = [int(n) for axis in data.split(',') for n in axis[2:].split('..')]
    return Cuboid((nums[0], nums[2], nums[4]), (nums[1], nums[3], nums[5]))


def parse_step(data):
    switch, cuboid = data.split(' ')
    return switch == 'on', parse_cuboid(cuboid)


def parse(data):
    return [parse_step(line) for line in data.split('\n')]


def reboot(steps, init):
    init_area = Cuboid((-50, -50, -50), (50, 50, 50))
    on = []
    for switch, cuboid in steps:
        if init and not cuboid.intersects(init_area):
            continue
        next = []
        for c in on:
            if cuboid.contains(c):
                continue
            elif cuboid.intersects(c):
                next.extend(cuboid.carve(c))
            else:
                next.append(c)
        if switch:
            next.append(cuboid)
        on = next
    return sum(c.volume for c in on)


if __name__ == "__main__":
    solve(22, parse, lambda x: reboot(x, True), lambda x: reboot(x, False))
