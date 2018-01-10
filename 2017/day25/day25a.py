#!/usr/bin/python

import re
import sys

class State:
    def __init__(self):
        self.tape = dict()
        self.pos = 0
        self.state = None

class Write:
    def __init__(self, value):
        self.value = value

    def run(self, state):
        state.tape[state.pos] = self.value

class Move:
    def __init__(self, offset):
        self.offset = offset

    def run(self, state):
        state.pos += self.offset

class SetState:
    def __init__(self, newstate):
        self.newstate = newstate

    def run(self, state):
        state.state = self.newstate


state = State()
nsteps = None

operations = dict()

op_state = None
op_value = None

ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    if not ln:
        ln = sys.stdin.readline()
        continue

    m = re.match('Begin in state ([A-Z]+)\.', ln)
    if m is not None:
        state.state = m.group(1)

    m = re.match('Perform a diagnostic checksum after (\d+) steps\.', ln)
    if m is not None:
        nsteps = int(m.group(1))

    m = re.match('In state ([A-Z]+):', ln)
    if m is not None:
        op_state = m.group(1)
        operations[op_state] = dict()

    m = re.match('If the current value is (\d+):', ln)
    if m is not None:
        op_value = int(m.group(1))
        operations[op_state][op_value] = []

    m = re.match('- Write the value (\d+)\.', ln)
    if m is not None:
        operations[op_state][op_value].append(Write(int(m.group(1))))

    m = re.match('- Move ([a-z]+) slot to the ([a-z]+)\.', ln)
    if m is not None:
        n = None
        if m.group(1) == 'one':
            n = 1
        if n is None:
            print 'whats',m.group(1)
            sys.exit(1)

        if m.group(2) == 'left':
            n *= -1
        elif m.group(2) == 'right':
            pass
        else:
            print 'whats',m.group(2)
            sys.exit(2)

        operations[op_state][op_value].append(Move(n))

    m = re.match('- Continue with state ([A-Z]+)\.', ln)
    if m is not None:
        operations[op_state][op_value].append(SetState(m.group(1)))

    ln = sys.stdin.readline()

for i in range(nsteps):
    curr_val = state.tape[state.pos] if state.pos in state.tape else 0
    for op in operations[state.state][curr_val]:
        op.run(state)

checksum = sum(state.tape.values())
print checksum
