#!/usr/bin/python

import sys

data = dict()
positions = ["up", "right", "down", "left"]

ln = sys.stdin.readline()
i = 0
while ln:
    ln = ln.strip()
    data[i] = dict()
    for j in range(len(ln)):
        data[i][j] = ln[j]
    ln = sys.stdin.readline()
    i += 1

x = int(len(data) / 2)
y = int(len(data[0]) / 2)

pos = 0
infections = 0


for _ in range(10000):
    if y not in data:
        data[y] = dict()
    if x not in data[y]:
        data[y][x] = '.'

    if data[y][x] == '#':
        pos = (pos + 1) % 4
        data[y][x] = '.'
    else:
        pos = (pos - 1) % 4
        data[y][x] = '#'
        infections += 1

    if pos == 0:
        y -= 1
    elif pos == 1:
        x += 1
    elif pos == 2:
        y += 1
    elif pos == 3:
        x -= 1

print infections
