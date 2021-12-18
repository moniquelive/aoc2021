#!/usr/bin/env python3

from dijkstar import Graph, find_path

maze = [[int(c) for c in line.strip()]
        for line in open('input-15.txt').readlines()]
# maze = [[int(c) for c in line]
#         for line in """1163751742
# 1381373672
# 2136511328
# 3694931569
# 7463417111
# 1319128137
# 1359912421
# 3125421639
# 1293138521
# 2311944581""".split()]


def neighbors_for(node):
    (x, y) = node
    return [(nx, ny)
            for nx, ny in [(x, y-1), (x, y+1), (x-1, y), (x+1, y)]
            if 0 <= nx < len(maze) and 0 <= ny < len(maze)]


def find(maze):
    graph = Graph()
    for j in range(len(maze)):
        for i in range(len(maze)):
            for n in neighbors_for((i, j)):
                graph.add_edge((i, j), n, maze[n[1]][n[0]])
    return find_path(graph, (0, 0), (len(maze)-1, len(maze)-1)).total_cost


print("part 1:", find(maze))


def s(a, b):
    if a + b > 9:
        return a + b - 9
    return a + b


n = len(maze)
maze = [line*5 for line in maze]*5
newmaze = []
for i, row in enumerate(maze):
    newmaze.append([s(r, i//n) for r in row])

for j, row in enumerate(newmaze):
    for i, col in enumerate(row):
        newmaze[j][i] = s(newmaze[j][i], i//n)

print("part 2:", find(newmaze))
