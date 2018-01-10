#!/usr/bin/python

target = 368078
total = 0

rowsize = 0
rowstart = 0
rowmid = 0
depth = 0

while total < target:
    if depth == 0:
        rowsize = 1
    elif depth == 1:
        rowsize = 8
    else:
        rowsize += 8
    depth += 1
    rowstart = total + 1
    rowmid = rowstart + depth - 2
    total += rowsize

toouter = depth - 1

rowmids = [rowmid + i * (depth - 1) * 2 for i in range(4)]
tomids = [abs(rowmids[i] - target) for i in range(4)]
tomid = min(tomids)

print toouter + tomid
