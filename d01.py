#!/usr/bin/env python

"""Advent of Code 2021, Day 1"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def increases(report, n):
    increases = 0
    prev = 0
    for curr in range(1, len(report) - n + 1):
        increases += sum(report[curr:curr+n]) > sum(report[prev:prev+n])
        prev = curr
    return increases


if __name__ == "__main__":
    solve(1, parse, lambda x: increases(x, 1), lambda x: increases(x, 3))
