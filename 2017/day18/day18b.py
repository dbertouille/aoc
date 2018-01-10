#!/usr/bin/python

import Queue
import sys

class program:
    def __init__(self, pid, instructions, qin, qout):
        self.instructions = instructions
        self.idx = 0
        self.pid = pid
        self.qin = qin
        self.qout = qout
        self.registers = dict()
        self.registers['p'] = pid
        self.sends = 0

    def get_register(self, t):
        if t not in self.registers:
            self.registers[t] = 0
        return self.registers[t]

    def set_register(self, t, v):
        self.registers[t] = v

    def get_register_or_constant(self, t):
        try:
            return int(t)
        except ValueError:
            return self.get_register(t)

    def run(self):
        toks = self.instructions[self.idx]

        if toks[0] == 'set':
            self.set_register(toks[1], self.get_register_or_constant(toks[2]))
            self.idx += 1

        if toks[0] == 'add':
            v = self.get_register(toks[1])
            v += self.get_register_or_constant(toks[2])
            self.set_register(toks[1], v)
            self.idx += 1

        if toks[0] == 'mul':
            v = self.get_register(toks[1])
            v *= self.get_register_or_constant(toks[2])
            self.set_register(toks[1], v)
            self.idx += 1

        if toks[0] == 'mod':
            v = self.get_register(toks[1])
            v %= self.get_register_or_constant(toks[2])
            self.set_register(toks[1], v)
            self.idx += 1

        if toks[0] == 'snd':
            self.qout.put(self.get_register_or_constant(toks[1]))
            self.idx += 1
            self.sends += 1

        if toks[0] == 'rcv':
            try:
                v = self.qin.get_nowait()
            except:
                return False
            self.set_register(toks[1], v)
            self.idx += 1

        if toks[0] == 'jgz':
            if self.get_register_or_constant(toks[1]) > 0:
                self.idx += self.get_register_or_constant(toks[2])
            else:
                self.idx += 1

        return True

instructions = []
ln = sys.stdin.readline()
while ln:
    instructions.append(ln.strip().split())
    ln = sys.stdin.readline()

queues = [Queue.Queue(), Queue.Queue()]

p0 = program(0, instructions, queues[0], queues[1])
p1 = program(1, instructions, queues[1], queues[0])

deadlock = False
while not deadlock:
    p0moved = p0.run()
    p1moved = p1.run()
    deadlock = (not p0moved and not p1moved)

print p1.sends
