#!/usr/bin/env python3

inputs = [tuple(l.strip().split(' | '))
          for l in open('input-08.txt').readlines()]


def one_four_seven_eight(lst):
    return len(list(filter(lambda d: len(d) in [2, 3, 4, 7], lst)))


# part 1: 1,4,7,8
#         1 : 2 segments
#         4 : 4 segments
#         7 : 3 segments
#         8 : 7 segments
print("part 1:", sum([one_four_seven_eight(d[1].split()) for d in inputs]))


def parse(parts):
    parts_set = sorted([set(p) for p in parts], key=len)
    parsed = {}
    parsed[1] = parts_set.pop(0)
    parsed[7] = parts_set.pop(0)
    parsed[4] = parts_set.pop(0)
    _235 = [parts_set.pop(0), parts_set.pop(0), parts_set.pop(0)]
    _069 = [parts_set.pop(0), parts_set.pop(0), parts_set.pop(0)]
    parsed[8] = parts_set.pop(0)

    for nine in _069:
        if nine.union(parsed[4]) != parsed[8]:
            parsed[9] = nine
    _069.remove(parsed[9])
    if _069[0].union(parsed[1]) != parsed[8]:
        parsed[0], parsed[6] = _069
    else:
        parsed[6], parsed[0] = _069

    for five in _235:
        if five.union(parsed[1]) == parsed[9]:
            parsed[5] = five
    _235.remove(parsed[5])
    if _235[0].union(parsed[1]) == _235[0]:
        parsed[3], parsed[2] = _235
    else:
        parsed[2], parsed[3] = _235

    return parsed  # { k: number, v: digits }


total = 0
for given_digits, encoded in inputs:
    parsed = parse(given_digits.split())
    current = ''.join([str(k) for d in encoded.split()
                      for k, v in parsed.items() if set(d) == v])
    total += int(current)

print("part 2:", total)
