#!/usr/bin/env python

"""Advent of Code 2021, Day 24"""

from itertools import product

from aoc import solve


def parse(data):
    program = [tuple(line.split(' ')) for line in data.split('\n')]
    return [tuple(int(program[i*18+x][2]) for x in [4, 5, 15]) for i in range(14)]


def find_model(params, digits, model, z):
    if len(model) == 14:
        return ''.join(map(str, model)) if z == 0 else None
    k1, k2, k3 = params[len(model)]
    modulo = ((z % 26) + k2)
    for digit in digits:
        x = int(modulo != digit)
        if k1 == 1 or (k1 == 26 and x == 0):
            model.append(digit)
            new_z = (z // k1) * ((25 * x) + 1) + (digit + k3) * x
            result = find_model(params, digits, model, new_z)
            if result:
                return result
            model.pop()


def model_high(params):
    return find_model(params, list(range(9, 0, -1)), [], 0)


if __name__ == "__main__":
    solve(24, parse, model_high)
