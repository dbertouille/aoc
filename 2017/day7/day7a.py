#!/usr/bin/python

import sys

p2c = dict()
base = None

ln = sys.stdin.readline()
while ln:
    toks = ln.strip().split()
    child = toks[0]
    if len(toks) > 2:
        for parent in [t.strip(',') for t in toks[3:]]:
            p2c[parent] = child
    else:
        base = child
    ln = sys.stdin.readline()

cur = base
while 1:
    if cur not in p2c:
        break
    cur = p2c[cur]
print cur
