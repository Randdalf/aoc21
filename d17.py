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
    while probe.pos.x <= tmax.x and probe.pos.y >= tmin.y:
        steps.append(probe.step())
        if probe.within(tmin, tmax):
            return steps
    return None


def apex_y(target):
    apex = 0
    tmin, tmax = target
    for vy in range(tmin.y, 300):
        for vx in range(1, tmax.x+1):
            steps = launch(*target, Vec2(vx, vy))
            if steps is None:
                continue
            apex = max(max(pos.y for pos in steps), apex)
    return apex


def initial_v(target):
    vels = []
    tmin, tmax = target
    for vy in range(tmin.y, 300):
        for vx in range(1, tmax.x+1):
            vel = Vec2(vx, vy)
            steps = launch(*target, vel)
            if steps is None:
                continue
            vels.append(vel)
    return len(vels)


if __name__ == "__main__":
    solve(17, parse, apex_y, initial_v)
