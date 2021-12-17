from os import truncate
import re

file = "./Day17/input.txt"
finalTotal = 0
input = []

#txMin = 20
#txMax = 30
#tyMin = -10
#tyMax = -5

txMin = 248
txMax = 285
tyMin = -85
tyMax = -56

failure = 1000

yVals = []
xVals = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())

def calcY(speed):
    y = 0
    spd = speed
    while y >= tyMax:
        y += spd
        spd -= 1
        if y >= tyMin and y <= tyMax:
            return True
    return False

def calcX(speed):
    x = 0
    spd = speed
    while x <= txMax:
        x += spd
        if spd > 0:
            spd -= 1
        if x >= txMin and x  <= txMax:
            return True
        if spd == 0:
            return False
    return False

def maxY(vX, vY):
    global txMax
    global tyMax
    global tyMin
    global txMin
    x = 0
    y = 0
    spdX = vX
    spdY = vY
    maxY = 0
    while x < txMax and y > tyMin:
        x += spdX
        y += spdY
        if(spdX > 0):
            spdX -= 1
        spdY -= 1
        if y > maxY:
            maxY = y
        if x >= txMin and x <= txMax and y >= tyMin and y <= tyMax:
            return [maxY, True]
    return [-1, False]


def part1():
    global xVals
    global yVals
    retVal = 0
    fails = 0
    speed = 1
    while fails < failure:
        tempY = calcY(speed)
        if tempY:
            yVals.append(speed)
            fails = 0
        else:
            fails += 1
        speed += 1
    speed = 1
    while speed <= txMax:
        tempX = calcX(speed)
        if tempX:
            xVals.append(speed)
        speed += 1
    for x in xVals:
        for y in yVals:
            temp = maxY(x, y)
            if(temp[0] > retVal):
                retVal = temp[0]
    print(retVal)

def part2():
    global xVals
    global yVals
    retVal = 0
    fails = 0
    speed = 0
    while fails < failure:
        tempY = calcY(speed)
        if tempY:
            yVals.append(speed)
            fails = 0
        else:
            fails += 1
        speed += 1
    fails = 0
    speed = -1
    while fails < failure:
        tempY = calcY(speed)
        if tempY:
            yVals.append(speed)
            fails = 0
        else:
            fails += 1
        speed -= 1
    speed = 1
    while speed <= txMax:
        tempX = calcX(speed)
        if tempX:
            xVals.append(speed)
        speed += 1
    for x in xVals:
        for y in yVals:
            temp = maxY(x, y)
            if temp[1]:
                retVal += 1
    print(retVal)

if __name__ == '__main__':
    parse()
    part2()