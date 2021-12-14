#!/usr/bin/env python

"""Advent of Code 2021, Day 14"""

from collections import Counter

from aoc import solve


def parse_rule(data):
    pair, elem = data.split(' -> ')
    return tuple(pair), elem


def parse(data):
    parts = data.split('\n\n')
    return list(parts[0]), dict(parse_rule(rule) for rule in parts[1].split('\n'))


def step(polymer, rules):
    result = []
    polymer.reverse()
    while len(polymer) > 1:
        a = polymer.pop()
        result.append(a)
        result.append(rules[(a, polymer[-1])])
    result.extend(polymer)
    return result


def common_elements(manual, steps=10):
    polymer, rules = manual
    for i in range(steps):
        polymer = step(polymer, rules)
    counts = Counter(polymer)
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    solve(14, parse, common_elements)
