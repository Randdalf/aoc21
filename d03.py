#!/usr/bin/env python

"""Advent of Code 2021, Day 3"""

from operator import eq, ne

from aoc import solve


def parse(data):
    return [[int(bit) for bit in line] for line in data.split('\n')]


def bin2dec(bits):
    return sum(bit << i for i, bit in enumerate(reversed(bits)))


def power_consumption(report):
    gamma_bits = [int(sum(bits) >= len(report) / 2) for bits in zip(*report)]
    epsilon_bits = [1 - bit for bit in gamma_bits]
    return bin2dec(gamma_bits) * bin2dec(epsilon_bits)


def test_criteria(report, criteria):
    pos = 0
    while len(report) > 1:
        common = int(sum(n[pos] for n in report) >= len(report) / 2)
        report = [bits for bits in report if criteria(bits[pos], common)]
        pos += 1
    return bin2dec(report[0])


def life_support(report):
    return test_criteria(report, eq) * test_criteria(report, ne)


if __name__ == "__main__":
    solve(3, parse, power_consumption, life_support)
