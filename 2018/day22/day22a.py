#!/usr/local/bin/python

depth = 4845
target = [6,770]
grid = []

for x in range(0,target[0]+1):
    row = []
    grid.append(row)
    for y in range(0, target[1]+1):
        if x == 0 and y == 0:
            gidx = 0
        elif x == target[0] and y == target[1]:
            gidx = 0
        elif y == 0:
            gidx = x * 16807
        elif x == 0:
            gidx = y * 48271
        else:
            gidx = grid[x-1][y] * grid[x][y-1]
        row.append((gidx + depth) % 20183)

risk = 0
for x in range(0, target[0]+1):
    for y in range(0, target[1]+1):
        m = grid[x][y] % 3
        risk += m
print risk
