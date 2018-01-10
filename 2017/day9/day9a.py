#!/usr/bin/python

import sys

ln = sys.stdin.readline().strip()

score = 0
depth = 0
escaped = False
state = 'group'
ngarbage = 0

for c in ln:
    if escaped:
        escaped = False
        continue

    if c == '!':
        escaped = True
        continue

    if state == 'group':
        if c == '{':
            depth += 1
        elif c == '}':
            score += depth
            depth -= 1
        elif c == '<':
            state = 'garbage'
    elif state == 'garbage':
        if c == '>':
            state = 'group'
        else:
            ngarbage += 1

print ngarbage
