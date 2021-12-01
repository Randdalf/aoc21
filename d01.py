#!/usr/bin/env python

"""Advent of Code 2021, Day 1"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split('\n')]


def increases(report, n):
    increases = 0
    prev = sum(report[:n])
    for i in range(1, len(report) - n + 1):
        curr = sum(report[i:i+n])
        increases += curr > prev
        prev = curr
    return increases


if __name__ == "__main__":
    solve(1, parse, lambda x: increases(x, 1), lambda x: increases(x, 3))
