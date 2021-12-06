#!/usr/bin/env python3

fishes = [int(i) for i in open('input-06.txt').read().split(',')]

def count(fishes, days):
    num_fishes = [0]*9 # ages
    for fish in fishes:
        num_fishes[fish] += 1

    for day in range(days):
        tmp = [0]*9
        for i in range(9):
            if i == 0:
                # each 0 spawns 6's and 8's
                tmp[6] = tmp[8] = num_fishes[0]
            else:
                # aging
                tmp[i-1] += num_fishes[i]
        num_fishes = tmp
    return sum(num_fishes)

print("part 1", count(fishes.copy(), 80))
print("part 2", count(fishes.copy(), 256))
