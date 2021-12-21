#!/usr/bin/env python

"""Advent of Code 2021, Day 21"""

from collections import Counter
from itertools import product

from aoc import solve


def parse(data):
    return [int(line.split(': ')[1]) - 1 for line in data.split('\n')]


def practice_dirac_dice(state, spaces=10, rolls=3, sides=100, win_score=1000):
    turn = 0
    turns = 0
    scores = [0, 0]
    die = 0
    while True:
        moves = 0
        for i in range(rolls):
            moves += 1 + die
            die = (die + 1) % sides
        state[turn] += moves
        scores[turn] += 1 + state[turn] % spaces
        turns += 1
        if scores[turn] >= win_score:
            return turns * min(scores) * rolls
        turn = 1 - turn


quantum_die = Counter(
    3 + i + j + k for i, j, k in product(range(3), range(3), range(3))
)


def diracursive(key, cache):
    if key in cache:
        return cache[key]
    wins = [0, 0]
    for moves, n in quantum_die.items():
        turn = key[0]
        state = list(key[1:3])
        scores = list(key[3:5])
        state[turn] += moves
        scores[turn] += 1 + state[turn] % 10
        if scores[turn] >= 21:
            wins[turn] += n
        else:
            result = diracursive((1 - turn, *state, *scores), cache)
            wins[0] += n * result[0]
            wins[1] += n * result[1]
    wins = tuple(wins)
    cache[key] = wins
    return wins


def real_dirac_dice(state):
    return max(diracursive((0, state[0], state[1], 0, 0), {}))


if __name__ == "__main__":
    solve(21, parse, practice_dirac_dice, real_dirac_dice)
