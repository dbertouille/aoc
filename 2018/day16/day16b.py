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
        for reg in args:
            if reg < 0 or reg >= len(self.regs):
                return False
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


count = 0
opcodemap = dict()
ln = sys.stdin.readline()
while ln:
    before = [int(x) for x in ln.strip().split('[')[1].strip(']').split(',')]
    code = [int(x) for x in sys.stdin.readline().strip().split()]
    after = [int(x) for x in sys.stdin.readline().strip().split('[')[1].strip(']').split(',')]
    ln = sys.stdin.readline().strip()
    ln = sys.stdin.readline().strip()

    if code[0] not in opcodemap:
        opcodemap[code[0]] = set(cmds)

    candidates = set()
    for cmd in cmds:
        cpu = CPU(copy.deepcopy(before))
        getattr(cpu, cmd)(code[1], code[2], code[3])
        if cpu.regs == after:
            candidates.add(cmd)
    opcodemap[code[0]] = opcodemap[code[0]].intersection(candidates)

changed = True
while changed:
    changed = False
    knownCodes = []
    for opcode,cmds in opcodemap.items():
        if len(cmds) == 1:
            knownCodes.append(list(cmds)[0])
    for opcode,cmds in opcodemap.items():
        if len(cmds) == 1:
            continue
        for cmd in knownCodes:
            if cmd in cmds:
                changed = True
                opcodemap[opcode].remove(cmd)

cpu = CPU([0,0,0,0])
ln = sys.stdin.readline()
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    code = [int(x) for x in ln.strip().split()]
    if code[0] not in opcodemap:
        print 'unknow opcode ',code[0]
        sys.exit(1)
    cmds = opcodemap[code[0]]
    if len(cmds) > 1:
        print 'more than one command for opcode ',code[0]
        sys.exit(1)
    getattr(cpu, list(cmds)[0])(code[1], code[2], code[3])
    ln = sys.stdin.readline()

print cpu.regs[0]
