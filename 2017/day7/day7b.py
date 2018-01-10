#!/usr/bin/python

import sys

n2w = dict()
p2c = dict()
c2p = dict()
childless = []
top = None

ln = sys.stdin.readline()
while ln:
    toks = ln.strip().split()
    parent = toks[0]
    if len(toks) > 3:
        children = [t.strip(',') for t in toks[3:]]
    else:
        children = []
        childless.append(parent)

    p2c[parent] = children
    for child in children:
        c2p[child] = parent
        
    n2w[parent] = int(toks[1].strip('()'))
    ln = sys.stdin.readline()

curr = childless[0]
while 1:
    if curr not in c2p:
        break
    curr = c2p[curr]
base = curr

def get_weight(node):
    return n2w[node] + sum([get_weight(child) for child in p2c[node]])

def find_wrong_weight(node, correct_weight):
    weights = dict()
    for child in p2c[node]:
        weights[child] = get_weight(child)

    correct_child_weight = max(set(weights.values()), key=weights.values().count)
    wrong_child = None
    for child, weight in weights.items():
        if weight != correct_child_weight:
            wrong_child = child
            break

    if wrong_child is None:
        return correct_weight - sum(weights.values())
    else:
        return find_wrong_weight(wrong_child, correct_child_weight)

print find_wrong_weight(base, None)
