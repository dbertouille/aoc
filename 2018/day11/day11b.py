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
maxSquareSize = None

squarePowerLevels = dict()

for s in range(1, 300):
    squarePowerLevels[s] = dict()
    print s,'/',300
    for x in range(1, 302-s):
        squarePowerLevels[s][x] = dict()
        for y in range(1, 302-s):
            if s == 1:
                squareLevel = grid[x][y]
            else:
                squareLevel = squarePowerLevels[s-1][x][y]

                for xp in range(x, x+s):
                    squareLevel += grid[xp][y+s-1]
                for yp in range(y, y+s-1):
                    squareLevel += grid[x+s-1][yp]

            if maxSquare is None or squareLevel > maxSquare:
                maxSquare = squareLevel
                maxSquareCoord = [x,y]
                maxSquareSize = s

            squarePowerLevels[s][x][y] = squareLevel

print maxSquareCoord, maxSquare, maxSquareSize
