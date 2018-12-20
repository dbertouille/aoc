#!/usr/local/bin/python

import sys

def printData(data):
    for row in data:
        for c in row:
            print c,
        print ''
    print ''

data = []
ln = sys.stdin.readline()
while ln:
    row = [c for c in ln.strip()]
    data.append(row)
    ln = sys.stdin.readline()

printData(data)
for i in range(10):
    newData = []
    for i in range(len(data)):
        newRow = []

        for j in range(len(data[i])):

            counts = {'.' : 0, '|' : 0, '#' : 0}
            for k in range(-1, 2):
                for l in range(-1, 2):
                    if k == 0 and l == 0:
                        continue
                    if (i+k) < 0 or (i+k) >= len(data):
                        continue
                    if (j+l) < 0 or (j+l) >= len(data[i+k]):
                        continue
                    counts[data[i+k][j+l]] += 1

            if data[i][j] == '.':
                if counts['|'] >= 3:
                    newRow.append('|')
                else:
                    newRow.append('.')
            elif data[i][j] == '|':
                if counts['#'] >= 3:
                    newRow.append('#')
                else:
                    newRow.append('|')
            elif data[i][j] == '#':
                if counts['#'] >= 1 and counts['|'] >= 1:
                    newRow.append('#')
                else:
                    newRow.append('.')

        newData.append(newRow)
    data = newData
    printData(data)

nly = 0
nt = 0
for row in data:
    for c in row:
        if c == '#':
            nly += 1
        if c == '|':
            nt += 1
print nly*nt
