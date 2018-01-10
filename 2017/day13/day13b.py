#!/usr/bin/python

import copy
import sys

og_firewall_states = dict()

ln = sys.stdin.readline()
while ln:
    toks = ln.split(':')
    state = dict({
        "size" : int(toks[1].strip()),
        "pos" : 0,
        "moving": "up",
    })
    og_firewall_states[int(toks[0])] = state
    ln = sys.stdin.readline()

nstates = max(og_firewall_states.keys()) + 1

found = True
delay = 0
while found:

    found = False
    firewall_states = og_firewall_states

    print delay
    for i in range(nstates):
        if i in firewall_states and firewall_states[i]["pos"] == 0:
            found = True

        for fstate in firewall_states.values():
            if state["size"] == 1:
                continue

            if fstate["moving"] == "up":
                fstate["pos"] += 1
                if fstate["pos"] == (fstate["size"] - 1):
                    fstate["moving"] = "down"
            else:
                fstate["pos"] -= 1
                if fstate["pos"] == 0:
                    fstate["moving"] = "up"

        if i == 0:
            og_firewall_states = copy.deepcopy(firewall_states)

        if found:
            delay += 1
            break

print delay
