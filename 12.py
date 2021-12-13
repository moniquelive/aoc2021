#!/usr/bin/env python3

from collections import defaultdict

lines = [tuple(line.strip().split('-'))
         for line in open('input-12.txt').readlines()]
# lines = [tuple(line.strip().split('-')) for line in [  # 10
#     "start-A",
#     "start-b",
#     "A-c",
#     "A-b",
#     "b-d",
#     "A-end",
#     "b-end"]]
# lines = [tuple(line.strip().split('-')) for line in [ # 19
#     "dc-end",
#     "HN-start",
#     "start-kj",
#     "dc-start",
#     "dc-HN",
#     "LN-dc",
#     "HN-end",
#     "kj-sa",
#     "kj-HN",
#     "kj-dc"]]

# lines = [tuple(line.strip().split('-')) for line in [  # 226
#     "fs-end",
#     "he-DX",
#     "fs-he",
#     "start-DX",
#     "pj-DX",
#     "end-zg",
#     "zg-sl",
#     "zg-pj",
#     "pj-he",
#     "RW-he",
#     "fs-DX",
#     "pj-RW",
#     "zg-RW",
#     "start-pj",
#     "he-WI",
#     "zg-he",
#     "pj-fs",
#     "start-RW"]]

graph = defaultdict(list)
for (f, t) in lines:
    graph[f].append(t)
    graph[t].append(f)


def paths1(graph, node, visited):
    if node == 'end':
        return 1
    count = 0
    for neighbor in graph[node]:
        if not neighbor.islower() or neighbor not in visited:
            count += paths1(graph, neighbor, visited | {node})
    return count


print("part 1:", paths1(graph, 'start', set()))


def paths2(graph, node, visited, visit_twice=True):
    if node == 'end':
        return 1
    count = 0
    for neighbor in graph[node]:
        if not neighbor.islower() or neighbor not in visited:
            count += paths2(graph, neighbor, visited | {neighbor}, visit_twice)
        elif visit_twice and neighbor not in {'start', 'end'}:
            count += paths2(graph, neighbor, visited | {neighbor}, False)
    return count


print("part 2:", paths2(graph, 'start', {'start'}))
