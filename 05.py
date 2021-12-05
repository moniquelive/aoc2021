#!/usr/bin/env python3

from collections import defaultdict

lines = [list(map(lambda l: list(map(int, l.split(','))), line.strip().split(' -> '))) for line
         in open('input-05.txt').readlines()]

m1 = defaultdict(int)
m2 = defaultdict(int)
for ((x1, y1), (x2, y2)) in lines:
    if x1 == x2:
        # vertical
        for y in range(min(y1, y2), max(y1, y2)+1):
            m1[(x1, y)] += 1
            m2[(x1, y)] += 1
    elif y1 == y2:
        # horizontal
        for x in range(min(x1, x2), max(x1, x2)+1):
            m1[(x, y1)] += 1
            m2[(x, y1)] += 1
    else:
        # diagonal
        assert x1 != x2 and y1 != y2
        assert abs(x1-x2) == abs(y1-y2)
        dx = -1 if x1 > x2 else +1
        dy = -1 if y1 > y2 else +1
        x, y = x1, y1
        while (x != x2) and (y != y2):
            m2[(x, y)] += 1
            x += dx
            y += dy
        m2[(x, y)] += 1
        assert x == x2 and y == y2

print("part 1:", len([v for v in m1.values() if v > 1]))
print("part 2:", len([v for v in m2.values() if v > 1]))
