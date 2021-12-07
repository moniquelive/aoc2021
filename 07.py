#!/usr/bin/env python3

subs = [int(i) for i in open('input-07.txt').read().split(',')]
#subs = [int(i) for i in '16,1,2,0,4,2,7,1,2,14'.split(',')]

all = []
for pivot in range(min(subs), max(subs)):
    all.append(sum([abs(pivot-sub) for sub in subs]))
print("part 1:", min(all))


def cost(a, b):
    n = abs(a-b)
    return n*(1+n)//2


all = []
for pivot in range(min(subs), max(subs)):
    s = sum([cost(pivot, sub) for sub in subs])
    #print(pivot, s, [cost(pivot, sub) for sub in subs])
    all.append(s)
print("part 2:", min(all))
