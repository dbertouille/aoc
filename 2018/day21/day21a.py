#!/usr/local/bin/python

import copy
import sys

cmds = [
    'addr',
    'addi',
    'mulr',
    'muli',
    'banr',
    'bani',
    'borr',
    'bori',
    'setr',
    'seti',
    'gtir',
    'gtri',
    'gtrr',
    'eqir',
    'eqri',
    'eqrr',
]

class CPU:
    def __init__(self, regs):
        self.regs = regs

    def _checkRegs(self, *args):
        # for reg in args:
        #    if reg < 0 or reg >= len(self.regs):
        #        return False
        return True

    def addr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        self.regs[dst] = self.regs[l] + self.regs[r]
        return True

    def addi(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        self.regs[dst] = self.regs[l] + r
        return True

    def mulr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        self.regs[dst] = self.regs[l] * self.regs[r]
        return True

    def muli(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        self.regs[dst] = self.regs[l] * r
        return True

    def banr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        self.regs[dst] = self.regs[l] & self.regs[r]
        return True

    def bani(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        self.regs[dst] = self.regs[l] & r
        return True

    def borr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        self.regs[dst] = self.regs[l] | self.regs[r]
        return True

    def bori(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        self.regs[dst] = self.regs[l] | r
        return True


    def setr(self, l, _, dst):
        if not self._checkRegs(l, dst):
            return False
        self.regs[dst] = self.regs[l]
        return True

    def seti(self, l, _, dst):
        if not self._checkRegs(dst):
            return False
        self.regs[dst] = l
        return True

    def gtir(self, l, r, dst):
        if not self._checkRegs(r, dst):
            return False
        if l > self.regs[r]:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True

    def gtri(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        if self.regs[l] > r:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True

    def gtrr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        if self.regs[l] > self.regs[r]:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True

    def eqir(self, l, r, dst):
        if not self._checkRegs(r, dst):
            return False
        if l == self.regs[r]:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True

    def eqri(self, l, r, dst):
        if not self._checkRegs(l, dst):
            return False
        if self.regs[l] == r:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True

    def eqrr(self, l, r, dst):
        if not self._checkRegs(l, r, dst):
            return False
        if self.regs[l] == self.regs[r]:
            self.regs[dst] = 1
        else:
            self.regs[dst] = 0
        return True


instructions= []

ipr = None

ln = sys.stdin.readline()
ipr = int(ln.strip().split()[1])

ln = sys.stdin.readline()
while ln:
    toks = ln.strip().split()
    cmd = toks[0]
    l = int(toks[1])
    r = int(toks[2])
    d = int(toks[3])
    instructions.append((cmd, l, r, d))
    ln = sys.stdin.readline()

cpu = CPU([0,0,0,0,0,0])
while cpu.regs[ipr] < len(instructions):
    if cpu.regs[ipr] == 28:
        print cpu.regs[3]
        sys.exit(0)
    # print cpu.regs," ",
    instruction = instructions[cpu.regs[ipr]]
    getattr(cpu, instruction[0])(*instruction[1:])
    # print cpu.regs
    cpu.regs[ipr] += 1
#print cpu.regs[0]
