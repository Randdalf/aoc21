#!/usr/bin/env python

"""Advent of Code 2021, Day 8"""

from aoc import solve


def parse_patterns(data):
    return [set(pattern) for pattern in data.split(' ')]


def parse_display(data):
    return [parse_patterns(part) for part in data.split(' | ')]


def parse(data):
    return [parse_display(line) for line in data.split('\n')]


def easy_digits(displays):
    uniq = {2, 3, 4, 7}
    return sum(int(len(o) in uniq) for s, os in displays for o in os)


if __name__ == "__main__":
    solve(8, parse, easy_digits)
