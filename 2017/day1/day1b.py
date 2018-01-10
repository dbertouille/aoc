#!/usr/bin/python

import sys

ln = sys.stdin.readline()
ln = ln.strip()

s = 0
for i in range(len(ln)):
    if ln[i] == ln[(i+len(ln) / 2) % len(ln)]:
        s += int(ln[i])
print s
