#!/usr/bin/python

import sys

vs = dict()

def get_var(k):
    if k not in vs:
        vs[k] = 0
    return vs[k]

def set_var(k, v):
    vs[k] = v

biggest = 0
ln = sys.stdin.readline()
while ln:
    toks = ln.strip().split()

    k = toks[0]
    op = toks[1]
    v = int(toks[2])
    cmp_k = toks[4]
    cmp_op = toks[5]
    cmp_v = int(toks[6])

    do_it = False
    if cmp_op == '>':
        do_it = (get_var(cmp_k) > cmp_v)
    elif cmp_op == '>=':
        do_it = (get_var(cmp_k) >= cmp_v)
    elif cmp_op == '<':
        do_it = (get_var(cmp_k) < cmp_v)
    elif cmp_op == '<=':
        do_it = (get_var(cmp_k) <= cmp_v)
    elif cmp_op == '==':
        do_it = (get_var(cmp_k) == cmp_v)
    elif cmp_op == '!=':
        do_it = (get_var(cmp_k) != cmp_v)

    if do_it:
        if op == 'inc':
            set_var(k, get_var(k) + v)
        else:
            set_var(k, get_var(k) - v)


    biggest = max(max(vs.values()), biggest)
    ln = sys.stdin.readline()

print biggest
