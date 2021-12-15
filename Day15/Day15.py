import re

file = "./Day15/input.txt"
finalTotal = 100000000000000
input = []
xMax = 0
yMax = 0

def parse():
    global input
    global xMax
    global yMax
    with open(file) as f:
        for line in f:
            vals = line.strip()
            arr = []
            for char in vals:
                arr.append(int(char))
            input.append(arr)
    xMax = len(input[0])
    yMax = len(input)

def checkRisk(risk):
    global finalTotal
    if risk < finalTotal:
        finalTotal = risk
        print(finalTotal)

def goPath(x, y, risk):
    global finalTotal
    if risk > finalTotal:
        return
    if(y < yMax - 1):
        goPath(x, y+1, risk + input[y+1][x])
    else:
        calcrisk = risk
        for i in range(x+1, xMax):
            calcrisk += input[y][i]
        checkRisk(calcrisk)
        return
    if(x < xMax - 1):
        goPath(x+1, y, risk + input[y][x+1])
    else:
        calcrisk = risk
        for i in range(y+1, yMax):
            calcrisk += input[i][x]
        checkRisk(calcrisk)
        return
    if x == xMax - 1 and y  == yMax - 1:
        checkRisk(risk)

def part1():
    goPath(0,0,0)
    print(finalTotal)

def part2():
    print("")

if __name__ == '__main__':
    parse()
    part1()