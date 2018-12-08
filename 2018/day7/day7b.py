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

minTime = 60
nworkers = 5
running = set()
ending = dict()
i = 0

while True:

    if i in ending:
        for c in ending[i]:
            running.remove(c)
            for k in rules:
                if c in rules[k]:
                    rules[k].remove(c)
   
    if len(rules) == 0 and len(running) == 0:
        break

    candidates = []
    for k in rules.keys():
        if len(rules[k]) == 0:
            candidates.append(k)
    sorted(candidates)

    for c in candidates:
        if len(running) < nworkers:
            del rules[c]
            running.add(c)
            endsAt = i + minTime + (ord(c) - ord('A')) + 1
            if endsAt not in ending:
                ending[endsAt] = []
            ending[endsAt].append(c)

    i += 1

print i
