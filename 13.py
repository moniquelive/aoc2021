#!/usr/bin/env python3

(coords, folds) = open('input-13.txt').read().split('\n\n')
# (coords, folds) = """6,10
# 0,14
# 9,10
# 0,3
# 10,4
# 4,11
# 6,0
# 6,12
# 4,1
# 0,13
# 10,12
# 3,4
# 3,0
# 8,4
# 1,10
# 2,14
# 8,10
# 9,0
#
# fold along y=7
# fold along x=5""".split('\n\n')

coords = [tuple([int(s) for s in c.split(',')])
          for c in coords.split()]
folds = [tuple(f.split(' ')[-1].split('='))
         for f in folds.split('\n')]


def gen_grid(grid, w, h):
    retval = ["." * (w + 1)] * (h + 1)
    for (x, y) in grid:
        line = list(retval[y])
        line[x] = '#'
        retval[y] = ''.join(line)
    return retval


def merge(a_list, b_list):
    # assert len(a_list) == len(b_list)
    # assert len(a_list[0]) == len(b_list[0])
    return [
        ''.join(['#' if '#' in {a, b} else '.'
                 for (a, b) in zip(a_line, b_line)])
        for (a_line, b_line) in zip(a_list, b_list)]


def fold(grid, how):
    axis, num = how[0], int(how[1])
    if axis == 'x':
        split = [(line[0:num], ''.join(reversed(line[num + 1:]))) for line in grid]
        first, second = list(map(lambda p: p[0], split)), list(map(lambda p: p[1], split))
        return merge(first, second)
    elif axis == 'y':
        first, second = grid[0:num], list(reversed(grid[num + 1:]))
        return merge(['.' * len(first[0])] * (len(second) - len(first)) + first,
                     ['.' * len(second[0])] * (len(first) - len(second)) + second)


grid = gen_grid(coords,
                max(coords, key=lambda p: p[0])[0],
                max(coords, key=lambda p: p[1])[1])
folded = fold(grid[:], folds[0])
print("part 1:", ''.join(folded).count('#'))

folded = grid[:]
for f in folds:
    folded = fold(folded, f)
print("part 2:")
print('\n'.join(folded).replace('.', ' '))
