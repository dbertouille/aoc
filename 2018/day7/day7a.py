#!/usr/local/bin/python

import sys

steps = set()
rules = dict()
ln = sys.stdin.readline()
while ln:
    toks = ln.split()
    steps.add(toks[1])
    steps.add(toks[7])
    if toks[7] not in rules:
        rules[toks[7]] = set()
    rules[toks[7]].add(toks[1])
    ln = sys.stdin.readline()

for s in steps:
    if s not in rules:
        rules[s] = set()

r = ''

while len(r) < len(steps):
    candidates = []
    for k in rules.keys():
        if len(rules[k]) == 0:
            candidates.append(k)
    sorted(candidates)
    if len(candidates) == 0:
        print 'could not find rule'
        sys.exit(0)
    r += candidates[0]
    del rules[candidates[0]]
    for k in rules.keys():
        if candidates[0] in rules[k]:
            rules[k].remove(candidates[0])

print r
