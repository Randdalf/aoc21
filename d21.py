#!/usr/bin/env python

"""Advent of Code 2021, Day 21"""

from aoc import solve


def parse(data):
    return [int(line.split(': ')[1]) - 1 for line in data.split('\n')]


def dirac_dice(state, spaces=10, rolls=3, sides=100, win_score=1000):
    turn = 0
    turns = 0
    scores = [0, 0]
    die = 0
    while True:
        moves = 0
        for i in range(rolls):
            moves += 1 + die
            die = (die + 1) % sides
        state[turn] = (state[turn] + moves) % spaces
        scores[turn] += 1 + state[turn]
        turns += 1
        if scores[turn] >= win_score:
            return turns * min(scores) * rolls
        turn = 1 - turn


if __name__ == "__main__":
    solve(21, parse, dirac_dice)
