#!/usr/bin/env python3

import operator as op

split = op.methodcaller('split')
lines = list(map(lambda x: tuple(split(x)), open('input-02.txt').readlines()))

aim = h_pos = depth_part1 = depth_part2 = 0
for (direction, amt) in lines:
    if direction == 'forward':
        h_pos += int(amt)
        depth_part2 += int(amt) * aim
    if direction == 'down':
        depth_part1 += int(amt)
        aim += int(amt)
    if direction == 'up':
        depth_part1 -= int(amt)
        aim -= int(amt)

print('part 1:', h_pos * depth_part1)
print('part 2:', h_pos * depth_part2)
