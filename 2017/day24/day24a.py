#!/usr/bin/python

import copy
import sys

ports = []

ln = sys.stdin.readline()
while ln:
    ports.append([int(t) for t in ln.strip().split('/')])
    ln = sys.stdin.readline()

def explore(used, npins):
    strongest = 0
    for port in used:
        strongest += port[0] + port[1]

    for port in ports:
        if port in used:
            continue

        if port[0] == npins:
            next_used = copy.deepcopy(used)
            next_used.append(port)
            strongest = max(strongest, explore(next_used, port[1]))
        elif port[1] == npins:
            next_used = copy.deepcopy(used)
            next_used.append(port)
            strongest = max(strongest, explore(next_used, port[0]))

    return strongest

strength = explore([], 0)
print strength
