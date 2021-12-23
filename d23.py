#!/usr/bin/env python

"""Advent of Code 2021, Day 23"""

from aoc import solve
from pathfind import bfs, astar, path_length, reconstruct_path

energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
stops = {
    # Hallways
    (1, 1): -1, (2, 1): -2, (4, 1): -3, (6, 1): -4,
    (8, 1): -5, (10, 1): -6, (11, 1): -7,
    # Rooms
    (3, 2): 1, (3, 3): 2, (5, 2): 3, (5, 3): 4,
    (7, 2): 5, (7, 3): 6, (9, 2): 7, (9, 3): 8
}
dests = {
    'A': {1, 2},
    'B': {3, 4},
    'C': {5, 6},
    'D': {7, 8}
}
inv_dests = {d: t for t, ds in dests.items() for d in ds}


class PrepassNode:
    def __init__(slf, pos, walls):
        slf.pos = pos
        slf.walls = walls

    def __hash__(slf):
        return hash(slf.pos)

    def __eq__(slf, otr):
        return slf.pos == otr.pos

    @property
    def _adjacencies(slf):
        x, y = slf.pos
        yield x - 1, y
        yield x + 1, y
        yield x, y - 1
        yield x, y + 1

    @property
    def neighbors(slf):
        for adj in slf._adjacencies:
            if adj in slf.walls:
                continue
            yield PrepassNode(adj, slf.walls)

    def dist(slf, neighbor):
        return 1


class Node:
    def __init__(slf, pods, dists, blockers):
        slf.pods = pods
        slf.dists = dists
        slf.blockers = blockers

    def __hash__(slf):
        return hash(slf.pods)

    def __eq__(slf, otr):
        return slf.pods == otr.pods

    def _blocked(slf, a, b, occupied):
        return not slf.blockers[(a, b)].isdisjoint(occupied)

    def _new(slf, i, type, stop):
        return Node(slf.pods[:i] + ((type, stop),) + slf.pods[i+1:], slf.dists, slf.blockers)

    @property
    def neighbors(slf):
        occupied = {stop for type, stop in slf.pods}
        polluted = {
            inv_dests[stop] for type, stop in slf.pods
            if stop in inv_dests and stop not in dests[type]
        }
        for i, (type, stop) in enumerate(slf.pods):
            if stop > 0:
                for hallway in range(-1, -8, -1):
                    if slf._blocked(stop, hallway, occupied):
                        continue
                    yield slf._new(i, type, hallway)
            elif type not in polluted:
                for dest in dests[type]:
                    if slf._blocked(stop, dest, occupied):
                        continue
                    yield slf._new(i, type, dest)

    def dist(slf, neighbor):
        for (a_t, a_s), (b_t, b_s) in zip(slf.pods, neighbor.pods):
            if a_s != b_s:
                return energy[a_t] * slf.dists[(a_s, b_s)]


def parse(data):
    pods = []
    walls = set()
    for y, line in enumerate(data.split('\n')):
        for x, cell in enumerate(line):
            pos = (x, y)
            if cell == '#':
                walls.add(pos)
            elif pos in stops and stops[pos] > 0:
                pods.append((cell, stops[pos]))
    pods.sort()
    return tuple(pods), walls


def least_energy(input):
    pods, walls = input

    # Precompute the shortest path between each stopping point, and the
    # potential obstructions along the way.
    dists = {}
    blockers = {}
    for a_pos, a_stop in stops.items():
        a_dists, prev = bfs(PrepassNode(a_pos, walls))
        for b_pos, b_stop in stops.items():
            key = (a_stop, b_stop)
            b_node = PrepassNode(b_pos, walls)
            dists[key] = a_dists[b_node]
            path = reconstruct_path(prev, b_node)
            if path:
                blockers[key] = {stops[node.pos] for node in path[1:] if node.pos in stops}
            else:
                blockers[key] = set()

    # Run the A* path finding algorithm over the graph of all amphipods
    # alternating between hallways and destination rooms.
    node = Node(pods, dists, blockers)

    def goal(node):
        return all(pos in dests[type] for type, pos in node.pods)

    def h(node):
        estimate = 0
        ideal = {'A': 1, 'B': 3, 'C': 5, 'D': 7}
        for type, stop in node.pods:
            if stop in dests[type]:
                continue
            estimate += energy[type] * dists[(stop, ideal[type])]
        return estimate

    return path_length(astar(node, goal, h))


if __name__ == "__main__":
    solve(23, parse, least_energy)
