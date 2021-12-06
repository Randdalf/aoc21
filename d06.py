#!/usr/bin/env python

"""Advent of Code 2021, Day 6"""

from aoc import solve


def parse(data):
    state = [0 for i in range(9)]
    for x in data.split(','):
        state[int(x)] += 1
    return state


def simulate(state, days):
    for day in range(days):
        state[7] += state[0]
        state = state[1:] + state[:1]
    return sum(state)


if __name__ == "__main__":
    solve(6, parse, lambda x: simulate(x, 80), lambda x: simulate(x, 256))
