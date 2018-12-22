#!/usr/local/bin/python

depth = 4845
target = [6,770]

# depth = 510
# target = [10, 10]
padding = 125

rock = '.'
wet = '='
narrow = '|'

nothing = '0'
torch = 'T'
climbing = 'C'

typeToTools = {
    rock: set([climbing,torch]),
    wet: set([climbing,nothing]),
    narrow: set([torch,nothing]),
}

def getMove(fromType, toType, fromMove, isToTarget):
    move = dict()
    toTools = typeToTools[toType]
    if isToTarget:
        toTools = set([torch])
    for tool,d in fromMove.items():
        for toTool in toTools:
            toold = d + 1
            if toTool != tool:
                toold += 7
                if toTool not in typeToTools[fromType]:
                    toold += 7
            if isToTarget and toTool != torch:
                toold += 7
            if toTool not in move or toold < move[toTool]:
                move[toTool] = toold
    return move

egrid = []
for x in range(0,target[0]+1+padding):
    row = []
    egrid.append(row)
    for y in range(0, target[1]+1+padding):
        if x == 0 and y == 0:
            gidx = 0
        elif x == target[0] and y == target[1]:
            gidx = 0
        elif y == 0:
            gidx = x * 16807
        elif x == 0:
            gidx = y * 48271
        else:
            gidx = egrid[x-1][y] * egrid[x][y-1]
        row.append((gidx + depth) % 20183)

tgrid = []
for x in range(0, target[0]+1+padding):
    row = []
    tgrid.append(row)
    for y in range(0, target[1]+1+padding):
        m = egrid[x][y] % 3
        if m == 0:
            row.append(rock)
        elif m == 1:
            row.append(wet)
        else:
            row.append(narrow)

"""
for y in range(target[1] + padding):
    for x in range(target[0] + padding):
        print tgrid[x][y],
    print ''
"""

dgrid = []
for x in range(0,target[0]+1+padding):
    row = []
    dgrid.append(row)
    for y in range(0,target[1]+1+padding):
        row.append(dict())

while True:
    changed = False

    for x in range(0, target[0]+padding):
        for y in range(0, target[1]+padding):
            if x == 0 and y == 0:
                dgrid[0][0][torch] = 0
                continue
            isToTarget = (x == target[0] and y == target[1])

            moves = []
            if x > 0:
                move = getMove(tgrid[x-1][y], tgrid[x][y], dgrid[x-1][y], isToTarget)
                moves.append(move)
            if y > 0:
                move = getMove(tgrid[x][y-1], tgrid[x][y], dgrid[x][y-1], isToTarget)
                moves.append(move)
            if dgrid[x+1][y]:
                move = getMove(tgrid[x+1][y], tgrid[x][y], dgrid[x+1][y], isToTarget)
                moves.append(move)
            if dgrid[x][y+1]:
                move = getMove(tgrid[x][y+1], tgrid[x][y], dgrid[x][y+1], isToTarget)
                moves.append(move)
            
            for move in moves:
                for tool, d in move.items():
                    if tool not in dgrid[x][y] or d < dgrid[x][y][tool]:
                        dgrid[x][y][tool] = d
                        changed = True

    if not changed:
        break

"""
for y in range(target[1] + padding):
    for x in range(target[0] + padding):
        print '[',
        for tool in dgrid[x][y]:
            print '%07s' % ('%s %s:%d' % (tgrid[x][y], tool, dgrid[x][y][tool])),
        print ']',
    print ''
"""

print dgrid[target[0]][target[1]]
