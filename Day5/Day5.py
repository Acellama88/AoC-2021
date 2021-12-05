import re
import numpy as np

file = "./Day5/input.txt"
input = []
coords = {}

def parse():
    with open(file) as f:
        for line in f:
            input.append(re.split(",| -> ",line.strip()))

def checkStraight(Line: list):
    if(Line[0] == Line[2]) or (Line[1] == Line[3]):
        return True
    return False

def getAdder(x0, y0, x1, y1):
    xDir = 0
    yDir = 0
    if(x0 < x1):
        xDir = 1
    elif (x1 < x0):
        xDir = -1
    if(y0 < y1):
        yDir = 1
    elif (y1 < y0):
        yDir = -1
    return (xDir, yDir)

def part1():
    for line in input:
        if checkStraight(line):
            x0 = int(line[0])
            y0 = int(line[1])
            x1 = int(line[2])
            y1 = int(line[3])
            addVal = getAdder(x0, y0, x1, y1)
            curX = x0
            curY = y0
            last = False
            while True:
                if f"{curX},{curY}" in coords:
                    coords[f"{curX},{curY}"] += 1
                else:
                    coords.update({f"{curX},{curY}":1})
                if last:
                    break
                curX += addVal[0]
                curY += addVal[1]
                if(curX == x1) and (curY == y1):
                    last = True
    totalCount = 0
    for val in coords.items():
        if(val[1] > 1):
            totalCount += 1
    print(totalCount)

def part2():
    for line in input:
        x0 = int(line[0])
        y0 = int(line[1])
        x1 = int(line[2])
        y1 = int(line[3])
        addVal = getAdder(x0, y0, x1, y1)
        curX = x0
        curY = y0
        last = False
        while True:
            if f"{curX},{curY}" in coords:
                coords[f"{curX},{curY}"] += 1
            else:
                coords.update({f"{curX},{curY}":1})
            if last:
                break
            curX += addVal[0]
            curY += addVal[1]
            if(curX == x1) and (curY == y1):
                last = True
    totalCount = 0
    for val in coords.items():
        if(val[1] > 1):
            totalCount += 1
    print(totalCount)   

if __name__ == '__main__':
    parse()
    part2()