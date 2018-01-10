#!/usr/bin/python

import copy
import sys

ports = []

ln = sys.stdin.readline()
while ln:
    ports.append([int(t) for t in ln.strip().split('/')])
    ln = sys.stdin.readline()

def explore(used, npins):
    longest = len(used)
    strongest = 0
    for port in used:
        strongest += port[0] + port[1]

    for port in ports:
        if port in used:
            continue

        if port[0] == npins:
            next_used = copy.deepcopy(used)
            next_used.append(port)
            next_longest, next_strongest = explore(next_used, port[1])
            if next_longest > longest or (next_longest == longest and next_strongest > strongest):
                longest = next_longest
                strongest = next_strongest
        elif port[1] == npins:
            next_used = copy.deepcopy(used)
            next_used.append(port)
            next_longest, next_strongest = explore(next_used, port[0])
            if next_longest > longest or (next_longest == longest and next_strongest > strongest):
                longest = next_longest
                strongest = next_strongest

    return longest, strongest

length, strength = explore([], 0)
print length, strength
