#!/usr/bin/env python

"""Advent of Code 2021, Day 12"""

from aoc import solve


class Cave:
    def __init__(slf, name):
        slf.name = name
        slf.big = name.isupper()
        slf.neighbors = []

    def __repr__(slf):
        return slf.name


def parse(data):
    caves = {}
    for edge in data.split('\n'):
        a, b = edge.split('-')
        if a not in caves:
            caves[a] = Cave(a)
        if b not in caves:
            caves[b] = Cave(b)
        caves[a].neighbors.append(caves[b])
        caves[b].neighbors.append(caves[a])
    return caves


def passages(caves):
    start = caves['start']
    prev = [([start], {start})]
    closed = []
    while len(prev) > 0:
        open = []
        for path, visited in prev:
            for neighbor in path[-1].neighbors:
                if neighbor.big or neighbor not in visited:
                    passage = (path + [neighbor], visited | {neighbor})
                    if neighbor.name == 'end':
                        closed.append(passage)
                    else:
                        open.append(passage)
        prev = open
    return len(closed)




if __name__ == "__main__":
    solve(12, parse, passages)
