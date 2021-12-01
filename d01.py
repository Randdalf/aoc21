#!/usr/bin/env python

"""Advent of Code 2021, Day 1"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def depth_increases(report):
    prev = report[0]
    increases = 0
    for measurement in report[1:]:
        increases += measurement > prev
        prev = measurement
    return increases


if __name__ == "__main__":
    solve(1, parse, depth_increases)
