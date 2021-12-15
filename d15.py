#!/usr/bin/env python

"""Advent of Code 2021, Day 15"""

from aoc import solve
from pathfind import dijkstra
from vec2 import Vec2

dirs = [
    Vec2(0, -1),
    Vec2(1, 0),
    Vec2(0, 1),
    Vec2(-1, 0)
]


class Cavern:
    def __init__(slf, risk, size):
        slf.risk = risk
        slf.size = size
        slf.goal = Vec2(size-1, size-1)


class Node:
    def __init__(slf, pos, cavern):
        slf.pos = pos
        slf.cavern = cavern

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def neighbors(slf):
        for dir in dirs:
            neighbor = slf.pos + dir
            if neighbor in slf.cavern.risk:
                yield Node(neighbor, slf.cavern)

    def dist(slf, neighbor):
        return slf.cavern.risk[neighbor.pos]


def parse(data):
    risk = {}
    rows = data.split('\n')
    for y, row in enumerate(rows):
        for x, tile in enumerate(row):
            risk[Vec2(x, y)] = int(tile)
    return Cavern(risk, len(rows))


def lowest_risk(cavern, repeat):
    if repeat > 1:
        risk = {}
        for ry in range(repeat):
            for rx in range(repeat):
                offset = Vec2(rx, ry) * cavern.size
                inc = rx + ry
                for pos in cavern.risk.keys():
                    risk[offset + pos] = (cavern.risk[pos] - 1 + inc) % 9 + 1
        cavern = Cavern(risk, cavern.size * repeat)

    def goal(node):
        return node.pos == cavern.goal

    path = dijkstra(Node(Vec2(0, 0), cavern), goal)
    return sum(cavern.risk[node.pos] for node in path[1:])


if __name__ == "__main__":
    solve(15, parse, lambda x: lowest_risk(x, 1), lambda x: lowest_risk(x, 5))
