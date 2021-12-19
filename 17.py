#!/usr/bin/env python3

from itertools import chain, takewhile, product
from math import sqrt, ceil, floor
import re

inp = open("./input-17.txt").readline()

m = re.match(r'target area: x=(-?\d+)..(-?\d+), y=(-?\d+)..(-?\d+)', inp)
x_min, x_max, y_min, y_max = map(int, m.groups())

print("part 1:", (y_min * (y_min + 1)) // 2)

lower = sqrt(0.25 + 2 * x_min) - 0.5
upper = sqrt(0.25 + 2 * x_max) - 0.5
# all positive ints between lower and upper are valid v_x if t ≥ v_x
joker_v_xs = range(ceil(lower), floor(upper) + 1)

valid_vv = set()

# max number of steps: - y_min * 2
for t in range(1, - y_min * 2 + 1):
    # find valid v_y
    v_y_min = y_min / t + t / 2 - 0.5
    v_y_max = y_max / t + t / 2 - 0.5

    valid_v_y = range(ceil(v_y_min), floor(v_y_max) + 1)

    # find valid v_x
    v_x_min = max(x_min / t + t / 2 - 0.5, t)
    v_x_max = x_max / t + t / 2 - 0.5
    valid_v_x = chain(range(ceil(v_x_min), floor(v_x_max) + 1),
                      takewhile(lambda v: v <= t, joker_v_xs))
    valid_vv.update(product(valid_v_x, valid_v_y))

print("part 2:", len(valid_vv))
