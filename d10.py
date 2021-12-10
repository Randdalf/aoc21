#!/usr/bin/env python

"""Advent of Code 2021, Day 10"""

from aoc import solve

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

opens = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

closes = {v: k for k, v in opens.items()}


def parse(data):
    return data.split('\n')


def syntax_errors(lines):
    total_score = 0
    for line in lines:
        stack = []
        for c in line:
            if c in opens:
                stack.append(c)
            elif stack[-1] != closes[c]:
                total_score += scores[c]
                break
            else:
                stack.pop()
    return total_score


if __name__ == "__main__":
    solve(10, parse, syntax_errors)
