#!/usr/local/bin/python

import sys

data = []
ln = sys.stdin.readline()
while ln:
    data.append(ln.strip())
    ln = sys.stdin.readline()

for i in range(len(data)):
    for j in range(len(data)):
        if len(data[i]) != len(data[j]):
            continue
        idx = 0
        n = 0
        for k in range(len(data[i])):
            if data[i][k] != data[j][k]:
                n += 1
                idx = k
            if n > 1:
                break
        if n == 1:
            print data[i][:idx] + data[i][idx+1:]
            sys.exit(0)
