#!/usr/bin/env python3

def count_growth(lst):
    return len(list(filter(lambda p: p[0] < p[1], zip(lst, lst[1:]))))


numbers = list(map(int, open('input-01.txt').readlines()))
print('part 1:', count_growth(numbers))

numbers = [sum(numbers[i:i+3]) for i in range(len(numbers) - 3 + 1)]
print('part 2:', count_growth(numbers))
