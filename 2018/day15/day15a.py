#!/usr/local/bin/python

import sys

class Unit:
    def __init__(self, typ, row, col):
        self.typ = typ
        self.hp = 200
        self.attack = 3
        self.row = row
        self.col = col
        self.moved = False

class Space:
    def __init__(self, typ):
        self.typ = typ
        self.unit = None

def printGrid(grid):
    for row in grid:
        for space in row:
            if space.unit is not None and space.unit.hp > 0:
                print space.unit.typ,
            else:
                print space.typ,
        print ''
    print ''

def printDGrid(grid):
    for row in grid:
        for d in row:
            print (d if d is not None else '-'),
        print ''
    print ''

def boundsCheck(grid, row, col):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[row]):
        return False
    return True

def addDistances(grid, dgrid, row, col, d):
    if not boundsCheck(grid, row, col):
        return
    if grid[row][col].typ == '#' or grid[row][col].unit is not None:
        return
    if dgrid[row][col] is not None and dgrid[row][col] <= d:
        return
    dgrid[row][col] = d
    addDistances(grid,dgrid,row-1,col,d+1)
    addDistances(grid,dgrid,row+1,col,d+1)
    addDistances(grid,dgrid,row,col-1,d+1)
    addDistances(grid,dgrid,row,col+1,d+1)

def getUnitToAttack(grid, unit, row, col, currentTarget):
    if not boundsCheck(grid, row, col):
        return currentTarget
    gridUnit = grid[row][col].unit
    if gridUnit is None or gridUnit.typ == unit.typ:
        return currentTarget
    if currentTarget is None or gridUnit.hp < currentTarget.hp:
        return gridUnit
    return currentTarget

def tryAttack(grid, unit):
    targetUnit = getUnitToAttack(grid, unit, unit.row-1, unit.col, None)
    targetUnit = getUnitToAttack(grid, unit, unit.row, unit.col-1, targetUnit)
    targetUnit = getUnitToAttack(grid, unit, unit.row, unit.col+1, targetUnit)
    targetUnit = getUnitToAttack(grid, unit, unit.row+1, unit.col, targetUnit)
    
    if targetUnit is None:
        return False

    targetUnit.hp -= unit.attack
    if targetUnit.hp <= 0:
        grid[targetUnit.row][targetUnit.col].unit = None

    return True

def isSpaceEmpty(grid, row, col):
    if row < 0 or row >= len(grid):
        return False
    if col < 0 or col >= len(grid[row]):
        return False
    return (grid[row][col].typ == '.' and grid[row][col].unit is None)

def getTargets(grid, unit):
    targets = []
    for unit in units:
        if space.unit.typ == unit.typ or unit.hp <= 0:
            continue
        if isSpaceEmpty(grid, unit.row-1,unit.col):
            targets.append([unit.row-1,unit.col])
        if isSpaceEmpty(grid, unit.row,unit.col-1):
            targets.append([unit.row,unit.col-1])
        if isSpaceEmpty(grid, unit.row,unit.col+1):
            targets.append([unit.row,unit.col+1])
        if isSpaceEmpty(grid, unit.row+1,unit.col):
            targets.append([unit.row+1,unit.col])
    # for target in targets:
    #    print 'Candidate targets for ',space.unit.typ,' at ',[space.unit.row,space.unit.col],': ',target
    return targets

grid = []
units = []
ln = sys.stdin.readline()
while ln:
    ln = ln.strip()
    row = []
    for c in ln:
        if c == '#':
            row.append(Space('#'))
        else:
            row.append(Space('.'))
        if c == 'G' or c == 'E':
            row[-1].unit = Unit(c, len(grid), len(row) - 1)
            units.append(row[-1].unit)

    grid.append(row)
    ln = sys.stdin.readline()

printGrid(grid)
rounds = 0

while True:
    # Check if the battle is won
    unitTypes = set()
    for unit in units:
        if unit.hp > 0:
            unitTypes.add(unit.typ)
    if len(unitTypes) < 2:
        break

    rounds += 1

    # Clear the moved attributed used to prevent double moves
    for row in grid:
        for space in row:
            if space.unit is not None:
                space.unit.moved = False

    for row in grid:
        for space in row:
            if space.unit is None or space.unit.moved:
                continue

            # First try and attack
            # If this succeeds no need to bother trying to move
            if tryAttack(grid, space.unit):
                print space.unit.typ,' at ',[space.unit.row,space.unit.col],' attacked'
                continue

            # Gets target spaces
            targets = getTargets(grid, space.unit)
            if len(targets) == 0:
                continue

            # Find distnaces to target spaces
            dGrid = []
            for _ in range(len(grid)):
                dRow = []
                for _ in range(len(grid[0])):
                    dRow.append(None)
                dGrid.append(dRow)
            for target in targets:
                addDistances(grid, dGrid, target[0], target[1], 0)
            # printDGrid(dGrid)

            # Find the shortest distance
            minD = None
            minDCol = None
            minDRow = None
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if (i == 0 and j == 0):
                        continue
                    if (i != 0 and j != 0):
                        continue
                    crow = space.unit.row+i
                    ccol = space.unit.col+j 
                    if crow < 0 or crow >= len(grid):
                        continue
                    if ccol < 0 or ccol >= len(grid[crow]):
                        continue
                    if dGrid[crow][ccol] is None:
                        continue
                    if minD is None or dGrid[crow][ccol] < minD:
                        minD = dGrid[crow][ccol]
                        minDRow = crow
                        minDCol = ccol
            if minD is None:
                print space.unit.typ,'[',space.unit.row,',', space.unit.col,'] cant move'
                continue

            # MOve and attack
            print 'Moving to ',minDRow,minDCol
            space.unit.row = minDRow
            space.unit.col = minDCol
            space.unit.moved = True
            grid[minDRow][minDCol].unit = space.unit
            space.unit = None
            tryAttack(grid, grid[minDRow][minDCol].unit)

    print 'After Round ',rounds
    printGrid(grid)
    for unit in units:
        print unit.typ,'[',unit.row,',',unit.col,'] HP: ',unit.hp
        
print 'combat ended after ',rounds,' rounds'
remHP = 0
for unit in units:
    if unit.hp > 0:
        remHP += unit.hp
print 'remaining hp ', remHP
print (rounds-1)*remHP
