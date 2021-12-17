#!/usr/bin/env python

"""Advent of Code 2021, Day 17"""

import re

from aoc import solve
from vec2 import Vec2


class Probe:
    def __init__(slf, vel):
        slf.pos = Vec2(0, 0)
        slf.vel = vel

    def step(slf):
        slf.pos += slf.vel
        if slf.vel.x > 0:
            slf.vel.x -= 1
        elif slf.vel.x < 0:
            slf.vel.x += 1
        slf.vel.y -= 1
        return slf.pos

    def within(slf, tmin, tmax):
        return (
            slf.pos.x >= tmin.x and
            slf.pos.x <= tmax.x and
            slf.pos.y >= tmin.y and
            slf.pos.y <= tmax.y
        )


def parse(data):
    pattern = re.compile(r'target area: x=(-?\d+)\.\.(-?\d+), y=(-?\d+)\.\.(-?\d+)')
    area = [int(n) for n in pattern.match(data).groups()]
    return Vec2(area[0], area[2]), Vec2(area[1], area[3])


def launch(tmin, tmax, vel):
    steps = []
    probe = Probe(vel)
    while probe.pos.x <= tmax.x and probe.pos.y >= tmax.y:
        steps.append(probe.step())
        if probe.within(tmin, tmax):
            return steps
    return None


def apex_y(target):
    tmin, tmax = target
    apex = 0
    for vy in range(1, 300):
        for vx in range(1, 10):
            steps = launch(tmin, tmax, Vec2(vx, vy))
            if steps is None:
                continue
            apex = max(max(pos.y for pos in steps), apex)
    return apex


if __name__ == "__main__":
    solve(17, parse, apex_y)
