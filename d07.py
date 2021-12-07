#!/usr/bin/env python

"""Advent of Code 2021, Day 7"""

from aoc import solve


def parse(data):
    return [int(x) for x in data.split(',')]


def min_fuel(crabs):
    return min(sum(abs(c - f) for c in crabs) for f in range(max(crabs)+1))


def tri(n):
    return (n*(n+1))//2


def min_fuel_tri(crabs):
    return min(sum(tri(abs(c - f)) for c in crabs) for f in range(max(crabs)+1))


if __name__ == "__main__":
    solve(7, parse, min_fuel, min_fuel_tri)
