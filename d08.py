#!/usr/bin/env python

"""Advent of Code 2021, Day 8"""

from collections import defaultdict, Counter

from aoc import solve

digits = {
    frozenset('abcefg'): 0,
    frozenset('cf'): 1,
    frozenset('acdeg'): 2,
    frozenset('acdfg'): 3,
    frozenset('bcdf'): 4,
    frozenset('abdfg'): 5,
    frozenset('abdefg'): 6,
    frozenset('acf'): 7,
    frozenset('abcdefg'): 8,
    frozenset('abcdfg'): 9
}


def parse_patterns(data):
    return [set(pattern) for pattern in data.split(' ')]


def parse_display(data):
    return [parse_patterns(part) for part in data.split(' | ')]


def parse(data):
    return [parse_display(line) for line in data.split('\n')]


def easy_digits(displays):
    return sum(int(len(o) in {2, 3, 4, 7}) for s, os in displays for o in os)


def sum_outputs(displays):
    wires = set('abcdefg')
    total = 0

    # Record the segments which occur for certain lengths.
    lens = defaultdict(set)
    for segments in digits.keys():
        lens[len(segments)].update(segments)

    # Record the frequencies at which segments occur.
    freqs = defaultdict(set)
    for segment, freq in Counter(s for segs in digits.keys() for s in segs).items():
        freqs[freq].add(segment)

    for signals, output in displays:
        # Analyse lengths and frequencies to map wires to segments.
        poss = defaultdict(lambda: set('abcdefg'))
        freq = defaultdict(int)
        for signal in signals:
            n = len(signal)
            for wire in signal:
                poss[wire] &= lens[n]
                freq[wire] += 1
        comb = {wire: poss[wire] & freqs[freq[wire]] for wire, segments in poss.items()}

        # Iteratively eliminate impossible assignments.
        mapping = {}
        while len(comb) > 0:
            swap = {}
            for wire, segments in comb.items():
                if len(segments) == 1:
                    mapping[wire] = segments.pop()
                else:
                    swap[wire] = {s for s in segments if s not in mapping.values()}
            comb = swap

        # Decode the output.
        decoded = 0
        for i, digit in enumerate(output):
            decoded *= 10
            decoded += digits[frozenset(mapping[wire] for wire in digit)]
        total += decoded

    return total


if __name__ == "__main__":
    solve(8, parse, easy_digits, sum_outputs)
