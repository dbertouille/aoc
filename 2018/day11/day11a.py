#!/usr/local/bin/python

maxPower = None
serial = 2866

grid = dict()

for x in range(1, 301):
    grid[x] = dict()
    for y in range(1, 301):
        rackID = x + 10
        powerLevel = rackID * y
        powerLevel += serial
        powerLevel *= rackID
        powerLevel = int(powerLevel / 100)
        powerLevel %= 10
        powerLevel -= 5

        grid[x][y] = powerLevel


maxSquare = None
maxSquareCoord = None

for x in range(1, 299):
    for y in range(1, 299):
        squareLevel = 0
        for xp in range(x,x+3):
            for yp in range(y,y+3):
                squareLevel += grid[xp][yp]
                if maxSquare is None or squareLevel > maxSquare:
                    maxSquare = squareLevel
                    maxSquareCoord = [x,y]

print maxSquareCoord, maxSquare
