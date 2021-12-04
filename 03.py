#!/usr/bin/env python3

def to_dec(lst):
    return int(''.join(map(str, lst)), 2)


lines = [list(map(int, list(line.strip())))
         for line in open('input-03.txt').readlines()]

ndigits = len(lines[0])
nlines = len(lines)

epsilon = [int([l[col] for l in lines].count(1) >= (nlines // 2))
           for col in range(ndigits)]
gamma = [1-x for x in epsilon]
print('part1:', to_dec(epsilon) * to_dec(gamma))

oxygen = lines[:]
col = 0
while len(oxygen) > 1:
    ones = [l[col] for l in oxygen].count(1)
    zeros = len(oxygen) - ones
    delta = ones - zeros
    keep = 1 if delta > 0 else 0 if delta < 0 else 1
    oxygen = list(filter(lambda line: line[col] == keep, oxygen))
    col += 1

co2 = lines[:]
col = 0
while len(co2) > 1:
    ones = [l[col] for l in co2].count(1)
    zeros = len(co2) - ones
    delta = ones - zeros
    keep = 0 if delta > 0 else 1 if delta < 0 else 0
    co2 = list(filter(lambda line: line[col] == keep, co2))
    col += 1

print('part2:', to_dec(oxygen[0]) * to_dec(co2[0]))
