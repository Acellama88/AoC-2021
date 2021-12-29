#Day 24 Calculated by Hand - See ReadMe for a link:
#Day 24 - Credit to kemmel-dev for their tutorial/guide on Day 24.  That put into context that which my brain could not!

import re
import math

file = "./Day24/input.txt"
number = "99599469198999"
numLoc = 0
input = []
output = []
offsets = [11, 12, 10, -8, 15, 15, -11, 10, -3, 15, -3, -1, -10, -16]
finalAdd = [8, 8, 12, 10, 2, 8, 4, 9, 10, 3, 7, 7, 2, 2]

w = 0
x = 0
y = 0
z = 0

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())

def clear():
    global numLoc, w, x, y, z
    w = 0
    x = 0
    y = 0
    z = 0
    numLoc = 0

def dec2bas26(val):
    wip = val
    retVal = 0
    while wip > 0:
        temp = wip % 10
        retVal = retVal * 26 + temp
        wip = math.floor(wip / 10)
    return retVal

def getVal(var):
    global w, x, y, z
    if var == "w":
        return w
    elif var == "x":
        return x
    elif var == "y":
        return y
    elif var == "z":
        return z
    else:
        return int(var)

def round(val):
    retVal = val
    if retVal >= 0:
        retVal = math.floor(retVal)
    else:
        retVal = math.floor(retVal + 1)
    return retVal

def storeVal(var, value):
    global w, x, y, z
    if var == "w":
        w = value
    elif var == "x": 
        x = value
    elif var == "y":
        y = value
    elif var == "z":
        z = value

def part1_2():
    global w, x, y, z, offsets
    for num in range(11111111111111,99999999999999):
        if str(num).find("0") >= 0:
            continue
        clear()
        val = str(num)
        complete = True
        for i in range(0,14):
            w = int(val[i])
            x = 0 if round(z / 26)+offsets[i] == w else 1
            y = w + (finalAdd[i] * x)
            if x == 1:
                z = z * 26 + y
            else:
                z = round(z / 26) + y
            if offsets[i] < 0 and x == 1:
                complete = False
                break
        if complete:
            print(num)

def part1():
    global number, numLoc, w, x, y, z
    #for i in range(1111,9999,1):
    #    if str(i).find("0") >= 0:
    #        continue
    #    number = str(i)
    if True:
        clear()
        for line in input:
            tokens = line.split(" ")
            retVal = 0
            a = 0
            b = 0
            if tokens[0] == "inp":
                retVal = int(number[numLoc])
                storeVal(tokens[1],retVal)
                numLoc += 1
            if tokens[0] == "add":
                a = getVal(tokens[1])
                b = getVal(tokens[2])
                retVal = a+b
                storeVal(tokens[1],retVal)
            if tokens[0] == "mul":
                a = getVal(tokens[1])
                b = getVal(tokens[2])
                retVal = a*b
                storeVal(tokens[1],retVal)
            if tokens[0] == "mod":
                a = getVal(tokens[1])
                b = getVal(tokens[2])
                retVal = a%b
                storeVal(tokens[1],retVal)
            if tokens[0] == "div":
                a = getVal(tokens[1])
                b = getVal(tokens[2])
                retVal = a / b
                if retVal >= 0:
                    retVal = math.floor(retVal)
                else:
                    retVal = math.floor(retVal + 1)
                storeVal(tokens[1],retVal)
            if tokens[0] == "eql":
                a = getVal(tokens[1])
                b = getVal(tokens[2])
                if a == b:
                    retVal = 1
                else:
                    retVal = 0
                storeVal(tokens[1],retVal)
            print(f"{line}: {tokens[1]} = {retVal} [ {w}, {x}, {y}, {z}]")

def part2():
    print()

if __name__ == '__main__':
    parse()
    #print(dec2bas26(1111))
    part1_2()