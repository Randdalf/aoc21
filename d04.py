#!/usr/bin/env python

"""Advent of Code 2021, Day 4"""

from aoc import solve


def parse(data):
    sections = data.split('\n\n')
    numbers = [int(n) for n in sections[0].split(',')]
    boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in sections[1:]]
    return numbers, boards


def score(board, drawn, last):
    return sum(n for row in board for n in row if n not in drawn) * last


def bingo(data):
    drawn = set()
    for number in data[0]:
        drawn.add(number)
        for board in data[1]:
            for row in range(5):
                if all(board[row][i] in drawn for i in range(5)):
                    return score(board, drawn, number)
            for col in range(5):
                if all(board[i][col] in drawn for i in range(5)):
                    return score(board, drawn, number)


if __name__ == "__main__":
    solve(4, parse, bingo)
