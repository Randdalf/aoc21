#!/usr/bin/env python

"""Advent of Code 2021, Day 14"""

from collections import Counter, defaultdict

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


def count_elements(a, b, rules, cache, depth):
    key = (a, b, depth)
    if key in cache:
        return cache[key]
    e = rules[(a, b)]
    counts = Counter(e)
    if depth > 1:
        counts.update(count_elements(a, e, rules, cache, depth - 1))
        counts.update(count_elements(e, b, rules, cache, depth - 1))
    cache[key] = counts
    return counts


def common_elements(manual, steps):
    polymer, rules = manual
    cache = {}
    counts = Counter(polymer)
    for a, b in zip(polymer, polymer[1:]):
        counts.update(count_elements(a, b, rules, cache, steps))
    return max(counts.values()) - min(counts.values())


if __name__ == "__main__":
    solve(14, parse, lambda x: common_elements(x, 10), lambda x: common_elements(x, 40))
