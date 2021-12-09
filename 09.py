#!/usr/bin/env python3

from collections import deque

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]
lines = [[int(d) for d in line.strip()]
         for line in open('input-09.txt').readlines()]

total = 0
for row in range(100):
    for col in range(100):
        neighbors = []
        if row == 0:
            if col == 0:
                neighbors = [lines[row][col+1], lines[row+1][col]]
            elif col == 99:
                neighbors = [lines[row][col-1], lines[row+1][col]]
            else:
                neighbors = [lines[row][col-1],
                             lines[row][col+1], lines[row+1][col]]
        elif row == 99:
            if col == 0:
                neighbors = [lines[row][col+1], lines[row-1][col]]
            elif col == 99:
                neighbors = [lines[row][col-1], lines[row-1][col]]
            else:
                neighbors = [lines[row][col-1],
                             lines[row][col+1], lines[row-1][col]]
        else:
            if col == 0:
                neighbors = [lines[row][col+1],
                             lines[row-1][col], lines[row+1][col]]
            elif col == 99:
                neighbors = [lines[row][col-1],
                             lines[row-1][col], lines[row+1][col]]
            else:
                neighbors = [lines[row][col-1], lines[row][col+1],
                             lines[row-1][col], lines[row+1][col]]
        if lines[row][col] < min(neighbors):
            total += lines[row][col] + 1
print("part 1:", total)


def go_deep_from(x, y, visited):
    num_visits = 0
    to_visit = deque(((x, y),))
    while to_visit:
        cx, cy = to_visit.popleft()
        if (cx, cy) in visited:
            continue
        visited.add((cx, cy))
        if lines[cy][cx] < 9:
            num_visits += 1
            for dx, dy in deltas:
                if 0 <= cx+dx < 100 and \
                   0 <= cy+dy < 100 and \
                   (cx+dx, cy+dy) not in visited:
                    to_visit.append((cx+dx, cy+dy))
    return num_visits


sinks_size = []
visited = set()

for y in range(100):
    for x in range(100):
        if (x, y) not in visited:
            sinks_size.append(go_deep_from(x, y, visited))
            visited.add((x, y))
total = sorted(sinks_size)[-3:]
print("part 2:", total[0] * total[1] * total[2])
