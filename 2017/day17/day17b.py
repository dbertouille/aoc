#!/usr/bin/python

from blist import blist

step = 314
data = blist([0])
pos = 0
n = 50000000

for i in range(n):
    if (i % 10000) == 0:
        print i
    pos = (pos + step) % len(data)
    data.insert(pos + 1, i + 1)
    pos += 1

print data[1]
