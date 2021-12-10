#!/usr/bin/env python

"""Advent of Code 2021, Day 10"""

from functools import reduce

from aoc import solve

error_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

autocomplete_scores = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

opens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

closes = {v: k for k, v in opens.items()}


class CorruptedError(Exception):
    def __init__(slf, c):
        slf.c = c


class IncompleteError(Exception):
    def __init__(slf, stack):
        slf.missing = [opens[c] for c in reversed(stack)]


def parse(data):
    return data.split('\n')


def process(line):
    stack = []
    for c in line:
        if c in opens:
            stack.append(c)
        elif stack[-1] != closes[c]:
            raise CorruptedError(c)
        else:
            stack.pop()
    if len(stack) > 0:
        raise IncompleteError(stack)


def syntax_errors(lines):
    total_score = 0
    for line in lines:
        try:
            process(line)
        except CorruptedError as err:
            total_score += error_scores[err.c]
        except IncompleteError:
            pass
    return total_score


def autocomplete(lines):

    def score(a, c):
        return a * 5 + autocomplete_scores[c]

    scores = []
    for line in lines:
        try:
            process(line)
        except IncompleteError as err:
            scores.append(reduce(score, err.missing, 0))
        except CorruptedError:
            pass
    scores.sort()
    return scores[len(scores) // 2]


if __name__ == "__main__":
    solve(10, parse, syntax_errors, autocomplete)
