#!/usr/bin/env python

"""Advent of Code 2021, Day 18"""

from aoc import solve


class RegularNumber:
    def __init__(slf, n):
        slf.n = n

    @property
    def regulars(slf):
        yield slf

    def find_exploded(slf, depth):
        return slf, None

    def split(slf):
        if slf.n >= 10:
            down = slf.n//2
            up = slf.n - down
            return SnailfishNumber(RegularNumber(down), RegularNumber(up)), True
        else:
            return slf, False

    @property
    def magnitude(slf):
        return slf.n

    def __repr__(slf):
        return repr(slf.n)


class SnailfishNumber:
    def __init__(slf, left, right):
        slf.left = left
        slf.right = right

    def __add__(slf, otr):
        sum = SnailfishNumber(slf, otr)
        sum.reduce()
        return sum

    @property
    def regulars(slf):
        yield from slf.left.regulars
        yield from slf.right.regulars

    def find_exploded(slf, depth):
        if depth == 4:
            return RegularNumber(0), (slf.left, slf.right)
        slf.left, exploded = slf.left.find_exploded(depth+1)
        if exploded:
            return slf, exploded
        slf.right, exploded = slf.right.find_exploded(depth+1)
        return slf, exploded

    def explode(slf):
        regulars = list(slf.regulars)
        _, exploded = slf.find_exploded(0)
        if not exploded:
            return False
        left, right = exploded
        left_idx = regulars.index(left)
        if left_idx > 0:
            regulars[left_idx-1].n += left.n
        right_idx = regulars.index(right)
        if right_idx < len(regulars) - 1:
            regulars[right_idx+1].n += right.n
        return True

    def split(slf):
        slf.left, action = slf.left.split()
        if action:
            return slf, action
        slf.right, action = slf.right.split()
        return slf, action

    def reduce(slf):
        while slf.explode() or slf.split()[1]:
            pass

    @property
    def magnitude(slf):
        return slf.left.magnitude * 3 + slf.right.magnitude * 2

    def __repr__(slf):
        return f'[{slf.left},{slf.right}]'


def parse_snailfish(it):
    c = next(it)
    if c == '[':
        left = parse_snailfish(it)
        next(it)
        right = parse_snailfish(it)
        next(it)
        return SnailfishNumber(left, right)
    else:
        return RegularNumber(int(c))


def parse(data):
    return [parse_snailfish(iter(line)) for line in data.split('\n')]


def final_sum(homework):
    return sum(homework[1:], homework[0]).magnitude


if __name__ == "__main__":
    solve(18, parse, final_sum)
