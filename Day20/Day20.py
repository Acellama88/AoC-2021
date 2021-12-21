import re

inputFile = "./Day20/input.txt"
keyFile = "./Day20/key.txt"
finalTotal = 0
input = []
key = ""
lights = {}

xMin = 0
yMin = 0
xMax = 0
yMax = 0

def parse():
    global xMax
    global yMax
    global key
    with open(inputFile) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())
                xMax = len(input[0])
                yMax = len(input)
    with open(keyFile) as k:
        for line in k:
            key = line.strip()

def doWork(steps):
    global xMin
    global yMin
    global xMax
    global yMax
    global lights
    global input
    extended = 0
    output = {}
    #create dictionary
    for y in range(len(input)):
        for x in range(len(input[0])):
            if input[y][x] == '#':
                lights[f"{x},{y}"] = True
    #bound range so we know we are always within
    xMin -= steps
    yMin -= steps
    xMax += steps
    yMax += steps

    for i in range(steps): #number of iterations
        for y in range(yMin,yMax+1):
            for x in range(xMin, xMax+1):
                #get binary
                bin = 0
                for b in range(y-1, y+2):
                    for a in range(x-1, x+2):
                        bin = bin << 1
                        if b < yMin or b > yMax or a < xMin or a > xMax:
                            bin |= extended
                        elif f"{a},{b}" in lights:
                            bin |= 1
                        else:
                            bin |= 0
                #get new value
                val = key[bin]
                if val == "#":
                    output[f"{x},{y}"] = True
        lights = output.copy()
        output.clear()
        extended = (extended + 1) % 2 #COMMENT OUT FOR EXAMPLE CODE BECAUSE AOC ARE JERKS!
    print(len(lights))

def part1():
    doWork(2)

def part2():
    doWork(50)

if __name__ == '__main__':
    parse()
    part2()