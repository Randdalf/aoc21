#!/usr/bin/env python

"""Advent of Code 2021, Day 12"""

from aoc import solve


class Cave:
    def __init__(slf, name):
        slf.big = name.isupper()
        slf.neighbors = []


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
    end = caves['end']
    open = [(start, {start}, slot)]
    closed = 0
    while len(open) > 0:
        head, visited, slot = open.pop()
        for neighbor in head.neighbors:
            if neighbor == end:
                closed += 1
            elif neighbor.big:
                open.append((neighbor, visited, slot))
            elif neighbor not in visited:
                open.append((neighbor, visited | {neighbor}, slot))
            elif neighbor != start and slot is None:
                open.append((neighbor, visited | {neighbor}, neighbor))
    return closed


if __name__ == "__main__":
    solve(12, parse, passages, lambda x: passages(x, None))
