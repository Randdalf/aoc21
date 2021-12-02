#!/usr/bin/env python

"""Advent of Code 2021, Day 2"""

from aoc import solve


class Sub1:
    def __init__(slf):
        slf.pos = 0
        slf.depth = 0

    def forward(slf, n):
        slf.pos += n

    def up(slf, n):
        slf.depth -= n

    def down(slf, n):
        slf.depth += n


class Sub2:
    def __init__(slf):
        slf.pos = 0
        slf.depth = 0
        slf.aim = 0

    def forward(slf, n):
        slf.pos += n
        slf.depth += n * slf.aim

    def up(slf, n):
        slf.aim -= n

    def down(slf, n):
        slf.aim += n


def parse(data):
    return [line.split(' ') for line in data.split('\n')]


def plot_course(course, sub):
    for instr, n in course:
        getattr(sub, instr)(int(n))
    return sub.pos * sub.depth


if __name__ == "__main__":
    solve(2, parse, lambda x: plot_course(x, Sub1()), lambda x: plot_course(x, Sub2()))
