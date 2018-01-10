#!/usr/bin/python

import sys

firewall_states = dict()

ln = sys.stdin.readline()
while ln:
    toks = ln.split(':')
    state = dict({
        "size" : int(toks[1].strip()),
        "pos" : 0,
        "moving": "up",
    })
    firewall_states[int(toks[0])] = state
    ln = sys.stdin.readline()

nstates = max(firewall_states.keys()) + 1

severity = 0
#print firewall_states
for i in range(nstates):
    if i in firewall_states and firewall_states[i]["pos"] == 0:
        severity += i * firewall_states[i]["size"]
        #print i

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

    # print firewall_states

print severity
