#!/usr/bin/python

import pprint
import sys

instructions = []
idx = 0
registers = dict()
last_snd = 0

def get_register(t):
    if t not in registers:
        registers[t] = 0
    return registers[t]

def set_register(t, v):
    registers[t] = v

def get_register_or_constant(t):
    try:
        return int(t)
    except ValueError:
        return get_register(t)

ln = sys.stdin.readline()
while ln:
    instructions.append(ln.strip().split())
    ln = sys.stdin.readline()

set_register('a', 1);

nmul = 0
while idx < len(instructions):
    toks = instructions[idx]
    
    if toks[0] == 'set':
        set_register(toks[1], get_register_or_constant(toks[2]))
        idx += 1
    elif toks[0] == 'sub':
        v = get_register(toks[1])
        v -= get_register_or_constant(toks[2])
        set_register(toks[1], v)
        idx += 1
    elif toks[0] == 'div':
        v = get_register(toks[1])
        v /= get_register_or_constant(toks[2])
        set_register(toks[1], v)
        idx += 1
    elif toks[0] == 'mod':
        v = get_register(toks[1])
        v %= get_register_or_constant(toks[2])
        set_register(toks[1], v)
        idx += 1
    elif toks[0] == 'mul':
        v = get_register(toks[1])
        v *= get_register_or_constant(toks[2])
        set_register(toks[1], v)
        idx += 1
        nmul += 1
    elif toks[0] == 'jnz':
        if get_register_or_constant(toks[1]) != 0:
            idx += get_register_or_constant(toks[2])
        else:
            idx += 1
    else:
        idx += 1

    pprint.pprint(registers)
print nmul
