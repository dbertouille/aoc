#!/usr/bin/python

import sys

words = set()

valid = 0
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    toks = [''.join(sorted(t)) for t in ln.split()]
    if len(toks) == len(set(toks)):
        valid += 1
    ln = sys.stdin.readline()
print valid
