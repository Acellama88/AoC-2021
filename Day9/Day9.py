import re

file = "./Day9/input.txt"
heatMap = []
lowpoints = []
basins = []
queue = []
xmin = 0
xmax = 0
ymin = 0
ymax = 0
basinCount = 0

def parse():
    global basinCount
    global xmin
    global xmax
    global ymin
    global ymax

    with open(file) as f:
        for line in f:
            data = []
            for i in range(len(line)):
                if line[i] >= '0' and line[i] <= '9':
                    data.append(int(line[i]))
            heatMap.append(data)
    xmax = len(heatMap[0])
    ymax = len(heatMap)

def part1():
    finalAnswer = 0
    xmin = 0
    xmax = len(heatMap[0])
    ymin = 0
    ymax = len(heatMap)
    for y in range(ymax):
        for x in range(xmax):
            val = heatMap[y][x]
            isSmallest = True
            if x != xmin:
                isSmallest = isSmallest and val < heatMap[y][x-1]
            if x != xmax - 1:
                isSmallest = isSmallest and val < heatMap[y][x+1]
            if y != ymin:
                isSmallest = isSmallest and val < heatMap[y-1][x]
            if y != ymax - 1:
                isSmallest = isSmallest and val < heatMap[y+1][x]
            if isSmallest:
                lowpoints.append(heatMap[y][x])
    for i in lowpoints:
        finalAnswer += i + 1
    print(finalAnswer)

def countBasin():
    global basinCount
    global xmin
    global xmax
    global ymin
    global ymax
    if len(queue) == 0:
        basins.append(basinCount)
        basinCount = 0
        return
    check = queue.pop()
    x = check[0]
    y = check[1]
    if heatMap[y][x] == -1:
        countBasin()
        return
    if x != xmin:
        val = heatMap[y][x-1]
        if val != 9 and val != -1:
            queue.append([x-1, y])
    if x != xmax - 1:
        val = heatMap[y][x+1]
        if val != 9 and val != -1:
            queue.append([x+1, y])
    if y != ymin:
        val = heatMap[y-1][x]
        if val != 9 and val != -1:
            queue.append([x, y-1])
    if y != ymax - 1:
        val = heatMap[y+1][x]
        if val != 9 and val != -1:
            queue.append([x, y+1])
    heatMap[y][x] = -1
    basinCount += 1
    countBasin()

def part2():
    global basinCount
    global xmin
    global xmax
    global ymin
    global ymax

    for y in range(ymax):
        for x in range(xmax):
            val = heatMap[y][x]
            if val == 9 or val == -1:
                continue
            else:
                queue.append([x,y])
                countBasin()
    basins.sort()
    max = len(basins)
    print(basins[max-1] * basins[max-2] * basins[max-3])

if __name__ == '__main__':
    parse()
    part2()