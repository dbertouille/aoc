#!/usr/local/bin/python

import sys

n2 = 0
n3 = 0

ln = sys.stdin.readline()
while ln:
    has2 = False
    has3 = False

    ln = ln.strip()
    n = dict()
    for c in ln:
        if c not in n:
            n[c] = 0
        n[c] += 1

    for c in n:
        if n[c] == 2:
            has2 = True
        if n[c] == 3:
            has3 = True

    if has2:
        n2 += 1
    if has3:
        n3 += 1

    ln = sys.stdin.readline()

print n2
print n3
print n2 * n3
