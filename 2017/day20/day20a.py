#!/usr/bin/python

import re
import sys

class particle:
    def __init__(self, p, v, a):
        self.p = p
        self.v = v
        self.a = a

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
    # for p in particles:
    #    print p.p[0],

    count += 1
    for p in particles:
        prev_md = p.md()
        p.v = add_tuples(p.v, p.a)
        p.p = add_tuples(p.p, p.v)

lowest_md_particle_idx = 0
for i in range(len(particles)):
    if particles[i].md() < particles[lowest_md_particle_idx].md():
        lowest_md_particle_idx = i

print lowest_md_particle_idx
