import re

file = "./Day25/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if True:
                input.append(list(line.strip()))
            else:
                input.append(list(filter(None,re.split(" |x|y|z|,|\.\.|=|\n",line))))

def part1():
    global input
    count = 0
    updated = True
    xMax = len(input[0])
    yMax = len(input)
    while updated:
        count += 1
        updated = False
        moveRight = []
        moveDown = []
        for step in range(0,2):
            for y in range(yMax):
                for x in range(xMax):
                    #East Movers First
                    if step == 0:
                        if input[y][x] == ">":
                            #check right
                            nextLoc = (x + 1) % xMax
                            if input[y][nextLoc] == ".":
                                #Move it!
                                moveRight.append([x,y])
                                updated = True
                    #South Movers Second
                    else:
                        if input[y][x] == "v":
                            #check down
                            nextLoc = (y + 1) % yMax
                            if input[nextLoc][x] == ".":
                                #Move it!
                                moveDown.append([x,y])
                                updated = True
            if step == 0:
                for i in moveRight:
                    y = i[1]
                    x = i[0]
                    nextX = (i[0] + 1) % xMax
                    input[y][x] = '.'
                    input[y][nextX] = '>'
            else:
                for i in moveDown:
                    y = i[1]
                    x = i[0]
                    nextY = (i[1] + 1) % yMax
                    input[y][x] = '.'
                    input[nextY][x] = 'v'

    print(count)


    print("")

if __name__ == '__main__':
    parse()
    part1()