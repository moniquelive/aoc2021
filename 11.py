#!/usr/bin/env python3

chars = [[int(c) for c in line.strip()]
         for line in open('input-11.txt').readlines()]

# chars = [[int(c) for c in line.strip()]
#          for line in [
#     "5483143223",
#     "2745854711",
#     "5264556173",
#     "6141336146",
#     "6357385478",
#     "4167524645",
#     "2176841721",
#     "6882881134",
#     "4846848554",
#     "5283751526"]]


def inc_neighbors(b, r, c):
    deltas = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)]

    for (dr, dc) in deltas:
        if 0 <= r+dr < 10 and 0 <= c+dc < 10:
            b[r+dr][c+dc] += 1


def propagate(board, flashed):
    flashes = 0
    for row in range(10):
        for col in range(10):
            if (row, col) in flashed:
                continue
            if board[row][col] > 9:
                flashed.add((row, col))
                flashes += 1
                inc_neighbors(board, row, col)
    for (row, col) in flashed:
        board[row][col] = 0
    return board, flashes


def step(board):
    new_board = [[(c+1) for c in l]
                 for l in board]
    total, flashed = 0, set()
    while True:
        (new_board, flashes) = propagate(new_board, flashed)
        total += flashes
        if flashes == 0:
            break
    return new_board, total


def all_zeroes(board):
    for row in range(10):
        if not all(n == 0 for n in board[row]):
            return False
    return True


def print_board(board):
    print('\n'.join([''.join(map(str, l)) for l in board]))


b = chars[:]
num_flashes = 0
for i in range(100):
    b, flashes = step(b)
    num_flashes += flashes
print("part 1:", num_flashes)

b = chars[:]
steps = 0
while not all_zeroes(b):
    b, _ = step(b)
    steps += 1

print("part 2:", steps)
