#!/usr/bin/env python

"""Advent of Code 2021, Day 16"""

from functools import reduce
from operator import mul

from aoc import solve

ops = {
    0: sum,
    1: lambda x: reduce(mul, x),
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1])
}


def biterate(bytes):
    for byte in bytes:
        for i in range(7, -1, -1):
            yield (byte & (1 << i)) >> i


def parse(data):
    return biterate(bytes.fromhex(data))


def take(bits, n):
    for i in range(n):
        yield next(bits)


def number(bits, n):
    num = 0
    for bit in take(bits, n):
        num = (num << 1) + bit
    return num


def literal(bits):
    lit = 0
    while True:
        start = next(bits)
        for bit in take(bits, 4):
            lit = (lit << 1) + bit
        if not start:
            break
    return lit


def version_sum(bits):
    ver = number(bits, 3)
    if number(bits, 3) == 4:
        literal(bits)
    elif number(bits, 1):
        for i in range(number(bits, 11)):
            ver += version_sum(bits)
    else:
        subs = take(bits, number(bits, 15))
        while True:
            try:
                ver += version_sum(subs)
            except RuntimeError:
                break
    return ver


def evaluate(bits):
    number(bits, 3)
    type_id = number(bits, 3)
    if type_id == 4:
        return literal(bits)
    operands = []
    if number(bits, 1):
        for i in range(number(bits, 11)):
            operands.append(evaluate(bits))
    else:
        subs = take(bits, number(bits, 15))
        while True:
            try:
                operands.append(evaluate(subs))
            except RuntimeError:
                break
    return ops[type_id](operands)


if __name__ == "__main__":
    solve(16, parse, version_sum, evaluate)
