#!/usr/bin/python

import sys

data = [
  ['.', '#', '.'],
  ['.', '.', '#'],
  ['#', '#', '#'],
]

rules = dict()

def get_subset(ioffset, joffset, n):
    subdata = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(data[ioffset * n + i][joffset * n + j])
        subdata.append(row)
    return subdata

def flatten(data):
    s = ''
    for row in data:
        for c in row:
            s += c
        if row != data[-1]:
            s += '/'
    return s

def add_rule(rule, transform):
    for _ in range(4):
        rules[flatten(rule)] = transform
        rule = zip(*rule[::-1])
    rule = list(reversed(rule))
    for _ in range(4):
        rules[flatten(rule)] = transform
        rule = zip(*rule[::-1])

ln = sys.stdin.readline()
while ln:
    rule_data, transform_data = ln.split('=>')

    rule = []
    rule_row_data = [t.strip() for t in rule_data.split('/')]
    for d in rule_row_data:
        rule.append([c for c in d])

    transform = []
    transform_row_data = [t.strip() for t in transform_data.split('/')]
    for d in transform_row_data:
        transform.append([c for c in d])
    
    add_rule(rule, transform)
    ln = sys.stdin.readline()

for _ in range(18):
    next_data = []
    size = len(data[0])

    if (size % 2) == 0:
        subsize = 2
    else:
        subsize = 3

    newdata = []
    for i in range(size / subsize):
        for _ in range(subsize + 1):
            newdata.append([])

        for j in range(size / subsize):
            subdata = get_subset(i, j, subsize)
            flatdata = flatten(subdata)
            transform = rules[flatdata]

            for k in range(len(transform)):
                for l in transform[k]:
                    newdata[i * (subsize + 1) + k].append(l)

    data = newdata

count = 0
for row in data:
    for c in row:
        if c == '#':
            count += 1

print count
