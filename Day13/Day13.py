import re

folds = [
    ["x",655],
    ["y",447],
    ["x",327],
    ["y",223],
    ["x",163],
    ["y",111],
    ["x",81],
    ["y",55],
    ["x",40],
    ["y",27],
    ["y",13],
    ["y",6]
]

file = "./Day13/input.txt"
finalTotal = 0
input = []
dots = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())
    for line in input:
        tokens = line.split(",")
        dots.append([int(tokens[0]),int(tokens[1])])

def foldIt():
    global dots
    global finalTotal
    for fold in folds:
        postFold = []
        if fold[0] == 'y':
            #fold up!
            line = fold[1]
            for dot in dots:
                if dot[1] < line:
                    postFold.append(dot)
                    continue
                else:
                    #fold it
                    y = dot[1]
                    y = line - (y - line)
                    if [dot[0],y] in dots:
                        continue
                    else:
                        postFold.append([dot[0],y])
        if fold[0] == 'x':
            #fold left!
            line = fold[1]
            for dot in dots:
                if dot[0] < line:
                    postFold.append(dot)
                    continue
                else:
                    #fold it
                    x = dot[0]
                    x = line - (x - line)
                    if [x,dot[1]] in dots:
                        continue
                    else:
                        postFold.append([x,dot[1]])
        dots.clear()
        dots = postFold
        if len(dots) > finalTotal:
            finalTotal = len(dots)

def part1():
    global finalTotal
    foldIt()
    print(finalTotal)

def part2():
    foldIt()
    xmax = 0
    ymax = 0
    for dot in dots:
        if dot[0] > xmax:
            xmax = dot[0]
        if dot[1] > ymax:
            ymax = dot[1]
    for y in range(ymax+1):
        out = ""
        for x in range(xmax+1):
            if [x,y] in dots:
                out += '#'
            else:
                out += "."
        print(out)

if __name__ == '__main__':
    parse()
    part1()