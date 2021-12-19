#!/usr/bin/env python

"""Advent of Code 2021, Day 19"""

from collections import defaultdict
from itertools import combinations, product

from aoc import solve


def parse_coord(data):
    return tuple(map(int, data.split(',')))


def parse_scanner(data):
    return [parse_coord(line) for line in data.split('\n')[1:]]


def parse(data):
    return [parse_scanner(part) for part in data.split('\n\n')]


def rotations():
    yield from product(range(4), range(4), range(4))


def rotate(coord, rotation):
    coord = list(coord)
    for axis, turns in enumerate(rotation):
        i = (axis - 1) % 3
        j = (axis + 1) % 3
        for turn in range(turns):
            coord[i], coord[j] = -coord[j], coord[i]
    return tuple(coord)


def add(c1, c2):
    return tuple(x1 + x2 for x1, x2 in zip(c1, c2))


def sub(c1, c2):
    return tuple(x1 - x2 for x1, x2 in zip(c1, c2))


def manhattan(c1, c2):
    return sum(abs(x1 - x2) for x1, x2 in zip(c1, c2))


def find_offset(u_coords, k_coords):
    for i, j in product(range(len(u_coords)), range(len(k_coords))):
        u_basis = u_coords[i]
        k_basis = k_coords[j]
        u_rel = {sub(u, u_basis) for u in u_coords}
        k_rel = {sub(k, k_basis) for k in k_coords}
        if len(u_rel & k_rel) >= 12:
            return sub(k_basis, u_basis)
    return None


def match_scanners(report):
    rotated = [{r: [rotate(c, r) for c in coords] for r in rotations()} for coords in report]
    unknown = list(range(1, len(report)))
    known = {0: ((0, 0, 0), (0, 0, 0))}
    beacons = {coord for coord in report[0]}
    while len(unknown) > 0:
        u = unknown.pop(0)
        for (u_rot, u_coords), (k, (k_rot, k_offset)) in product(rotated[u].items(), known.items()):
            offset = find_offset(u_coords, rotated[k][k_rot])
            if offset is not None:
                u_offset = add(offset, k_offset)
                beacons.update(add(coord, u_offset) for coord in u_coords)
                known[u] = (u_rot, u_offset)
                break
        if u not in known:
            unknown.append(u)
    return beacons, known


def beacons(report):
    return len(match_scanners(report)[0])


def largest_dist(report):
    known = match_scanners(report)[1]
    return max(manhattan(a, b) for a, b in combinations((x[1] for x in known.values()), 2))


if __name__ == "__main__":
    solve(19, parse, beacons, largest_dist)
