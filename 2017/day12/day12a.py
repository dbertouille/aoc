#!/usr/bin/python

import sys

pipes = dict()

ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    toks = ln.split(' ', 2)
    src = toks[0]
    pipes[src] = set([t.strip() for t in toks[2].split(',')])
    ln = sys.stdin.readline()

s = set()

def process(src):
    if src in s:
        return
    s.add(src)
    for dst in pipes[src]:
        process(dst)

print s
