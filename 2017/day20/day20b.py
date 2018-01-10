#!/usr/bin/python

import re
import sys

class particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a
        self.destroyed = False

    def md(self):
        return abs(self.p[0]) + abs(self.p[1]) + abs(self.p[2])

def parse_tuple(s):
    s = s.strip('<')
    s = s.strip('>')
    return [int(t) for t in s.split(',')]

def add_tuples(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1], + t1[2] + t2[2])

particles = []
ln = sys.stdin.readline()
while ln:
    matches = re.findall('<[^>]+>', ln)
    particles.append(particle(
        parse_tuple(matches[0]),
        parse_tuple(matches[1]),
        parse_tuple(matches[2])))
    ln = sys.stdin.readline()

count = 0
while count < 10000:
    count += 1

    for p in particles:
        prev_md = p.md()
        p.v = add_tuples(p.v, p.a)
        p.p = add_tuples(p.p, p.v)

    d = dict()
    for p in particles:
        if p.p not in d:
            d[p.p] = []
        d[p.p].append(p)

    for k in d:
        if len(d[k]) == 1:
            continue
        for p in d[k]:
            p.destroyed = True

count = 0
for p in particles:
    if not p.destroyed:
        count += 1
print count
