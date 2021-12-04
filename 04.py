#!/usr/bin/env python3

import itertools


def parse(board):
    return [list(map(int, line.split())) for line in board]


def full_row(b, lst):
    set_lst = set(lst)
    for row in b:
        if set(row) <= set_lst:
            return True
    return False


def full_col(b, lst):
    return full_row([list(row) for row in zip(*b)], lst)


def winner(b, draws):
    if len(draws) < 5:
        return False
    return full_row(b, draws) or full_col(b, draws)


def score(b, balls):
    flatten = set(itertools.chain.from_iterable(b))
    return balls[-1] * (sum(flatten-set(balls)))


lines = [line.strip() for line in open('input-04.txt').readlines()]
draw_order = list(map(int, lines.pop(0).split(',')))

assert len(lines) % 6 == 0
boards = [parse(lines[x:x+5]) for x in (range(1, len(lines), 6))]

first_winner, first_balls = None, None
last_verified = None
for i, d in enumerate(draw_order):
    balls = draw_order[0:1+i]
    verified = [winner(board, balls) for board in boards]
    if any(verified) and not first_winner:
        first_winner = boards[verified.index(True)]
        first_balls = balls
    if all(verified):
        break
    last_verified = verified

print('part 1:', score(first_winner, first_balls))
print('part 2:', score(boards[last_verified.index(False)], balls))
