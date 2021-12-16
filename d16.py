#!/usr/bin/env python

"""Advent of Code 2021, Day 16"""

from aoc import solve


def parse(data):
    return bytes.fromhex(data)


def biterate(bytes):
    for byte in bytes:
        for i in range(7, -1, -1):
            yield (byte & (1 << i)) >> i


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


def packet(bits):
    ver = number(bits, 3)
    if number(bits, 3) == 4:
        literal(bits)
    elif number(bits, 1):
        for i in range(number(bits, 11)):
            ver += packet(bits)
    else:
        subs = take(bits, number(bits, 15))
        while True:
            try:
                ver += packet(subs)
            except RuntimeError:
                break
    return ver


def version_sum(transmission):
    return packet(biterate(transmission))


if __name__ == "__main__":
    solve(16, parse, version_sum)
