#!/usr/local/bin/python

import sys

ln = sys.stdin.readline()
data = dict()

while ln:
    ln = ln.strip()
    claimID, _, loc, sz = ln.split()
    x, y = loc.strip(':').split(',')
    w, h = sz.split('x')
    for i in range(int(x),int(x)+int(w)):
        if i not in data:
            data[i] = dict()
        for j in range(int(y), int(y)+int(h)):
            if j not in data[i]:
                data[i][j] = 0
            data[i][j] += 1
    ln = sys.stdin.readline()

c = 0
for x in data.keys():
    for y in data[x].keys():
        if data[x][y] > 1:
            c += 1
print c
