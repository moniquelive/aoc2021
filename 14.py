#!/usr/bin/env python3

from collections import Counter

(polymer, pairs) = open('input-14.txt').read().split('\n\n')
# (polymer, pairs) = """NNCB

# CH -> B
# HH -> N
# CB -> H
# NH -> C
# HB -> C
# HC -> B
# HN -> C
# NN -> C
# BH -> H
# NC -> B
# NB -> B
# BN -> B
# BB -> N
# BC -> B
# CC -> N
# CN -> C""".split('\n\n')

pairs = {p[0]: p[1]
         for p in [line.split(' -> ') for line in pairs.splitlines()]}


def string_to_list_in_pairs(s):
    return [''.join(pair) for pair in zip(s[:-1], s[1:])]


def replace_pair(p):
    return p[0] + pairs[p] + p[1] if p in pairs else p


def join(lst):
    return ''.join([x[0:2] for x in lst[0:-1]] + [lst[-1]])


def iter(poly):
    return join(list(map(replace_pair, string_to_list_in_pairs(poly))))


pol = polymer[:]
for _ in range(10):
    pol = iter(pol)
c = Counter(pol).most_common()
most = c[0][1]
least = c[-1][1]
print("part 1:", most-least)


pol = polymer[:]
count = Counter(map(''.join, zip(pol, pol[1:])))

for _ in range(40):
    for key, n in count.copy().items():
        count[key] -= n
        middle = pairs[key]
        first, second = key
        count[first + middle] += n
        count[middle + second] += n

totals = Counter()
for (first, second), n in count.items():
    totals[first] += n
    totals[second] += n
(_, most), *_, (_, least) = totals.most_common()

print("part 2:", (most - least) // 2)
