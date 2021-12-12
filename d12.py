#!/usr/bin/env python

"""Advent of Code 2021, Day 12"""

from collections import defaultdict

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


def passages(caves, slot='unused'):
    start = caves['start']
    prev = [([start], {start}, slot)]
    closed = []
    while len(prev) > 0:
        open = []
        for path, visited, slot in prev:
            for neighbor in path[-1].neighbors:
                passage = None
                if neighbor.big:
                    passage = (path + [neighbor], visited, slot)
                elif neighbor not in visited:
                    passage = (path + [neighbor], visited | {neighbor}, slot)
                elif neighbor != start and slot is None:
                    passage = (path + [neighbor], visited | {neighbor}, neighbor)
                if passage:
                    if neighbor.name == 'end':
                        closed.append(passage)
                    else:
                        open.append(passage)
        prev = open
    return len(closed)


if __name__ == "__main__":
    solve(12, parse, passages, lambda x: passages(x, None))
