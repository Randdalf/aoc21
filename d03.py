#!/usr/bin/env python

"""Advent of Code 2021, Day 3"""

from aoc import solve


def parse(data):
    return [[int(bit) for bit in line] for line in data.split('\n')]


def power_consumption(report):
    sums = [0 for b in report[0]]
    for number in report:
        for i, bit in enumerate(number):
            sums[i] += 2 * bit - 1
    gamma = 0
    epsilon = 0
    for i, sum in enumerate(reversed(sums)):
        if sum > 0:
            gamma += 1 << i
        else:
            epsilon += 1 << i
    return gamma * epsilon


if __name__ == "__main__":
    solve(3, parse, power_consumption)
