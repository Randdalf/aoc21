#!/usr/bin/env python

"""Advent of Code 2021, Day 13"""

from aoc import solve


def parse_dot(data):
    return tuple(int(x) for x in data.split(','))


def parse_instr(data):
    axis, n = data[11:].split('=')
    return (axis, int(n))


def parse(data):
    parts = data.split('\n\n')
    dots = {parse_dot(dot) for dot in parts[0].split('\n')}
    instrs = [parse_instr(instr) for instr in parts[1].split('\n')]
    return dots, instrs


def fold_axis(x, n):
    return n - abs(x - n)


def fold_x(dot, n):
    return (fold_axis(dot[0], n), dot[1])


def fold_y(dot, n):
    return (dot[0], fold_axis(dot[1], n))


def fold_paper(manual, limit=None):
    dots, instrs = manual
    for axis, n in instrs[:limit]:
        fold = fold_x if axis == 'x' else fold_y
        dots = {fold(dot, n) for dot in dots}
    return dots


def count_dots(manual):
    return len(fold_paper(manual, 1))


def print_code(manual):
    dots = fold_paper(manual)
    size = tuple(1 + max(dot[i] for dot in dots) for i in range(2))
    code = ''
    for y in range(size[1]):
        for x in range(size[0]):
            code += ''.join('#' if (x, y) in dots else ' ')
        code += '\n'
    return code


if __name__ == "__main__":
    solve(13, parse, count_dots, print_code)
