#!/usr/bin/python

import sys

data = []

ln = sys.stdin.readline()
while ln:
    data.append(int(ln.strip()))
    ln = sys.stdin.readline()

idx = 0
nsteps = 0
while idx >= 0 and idx < len(data):
    p = data[idx]
    data[idx] += (1 if data[idx] < 3 else -1)
    idx += p
    nsteps += 1
print nsteps

