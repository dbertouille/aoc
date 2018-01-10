#!/usr/bin/python

from blist import blist

step = 314
data = blist([0])
pos = 0
n = 2017

for i in range(n):
    pos = (pos + step) % len(data)
    data.insert(pos + 1, i + 1)
    pos += 1

print data[pos + 1]
