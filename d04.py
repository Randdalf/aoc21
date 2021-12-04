#!/usr/bin/env python

"""Advent of Code 2021, Day 4"""

from aoc import solve


class Input:
    def __init__(slf, numbers, boards):
        slf.numbers = numbers
        slf.boards = boards


def parse(data):
    sections = data.split('\n\n')
    numbers = [int(n) for n in sections[0].split(',')]
    boards = [[[int(n) for n in row.split()] for row in board.split('\n')] for board in sections[1:]]
    return Input(numbers, boards)


def winner(board, drawn):
    for row in range(5):
        if all(board[row][i] in drawn for i in range(5)):
            return True
    for col in range(5):
        if all(board[i][col] in drawn for i in range(5)):
            return True
    return False


def score(board, drawn, last):
    return sum(n for row in board for n in row if n not in drawn) * last


def bingo_first(input):
    drawn = set()
    for number in input.numbers:
        drawn.add(number)
        for board in input.boards:
            if winner(board, drawn):
                return score(board, drawn, number)


def bingo_last(input):
    drawn = set()
    for number in input.numbers:
        drawn.add(number)
        boards = [board for board in input.boards if not winner(board, drawn)]
        if len(boards) == 0:
            return score(input.boards[0], drawn, number)
        input.boards = boards


if __name__ == "__main__":
    solve(4, parse, bingo_first, bingo_last)
