from os import truncate
import heapq
import re

file = "./Day15/input.txt"
input = []
xMax = 0
yMax = 0

queue = []
inQueue = {}
visited = {}

def sortQ(value):
    return value[2]

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

def checkInQueue(x, y):
    global queue
    for node in queue:
        if node[0] == x and node[1] == y:
            return queue.index(node)
    return -1

def updateQueue(x, y, distance):
    global queue
    if f"{x},{y}" in visited:
        return
    loc = checkInQueue(x, y)
    if loc >= 0:
        #check distance and update
        if queue[loc][2] > distance:
            queue[loc][2] = distance
    else:
        heapq.heappush(queue, [x, y, distance])

def performMagic():
    global input
    global queue
    global xMax
    global yMax
    while len(queue) > 0:
        #get smallest list item
        queue.sort(key=sortQ)
        node = heapq.heappop(queue)
        x = node[0]
        y = node[1]
        dist = node[2]
        if x > 0: #Check to the Left
            newDist = dist + input[y][x - 1]
            updateQueue(x - 1, y, newDist)
        if x < xMax - 1: #Check to the Right
            newDist = dist + input[y][x + 1]
            updateQueue(x + 1, y, newDist)
        if y > 0: #Check to the Top
            newDist = dist + input[y - 1][x]
            updateQueue(x, y - 1, newDist)
        if y < yMax - 1: #Check to the Bottom
            newDist = dist + input[y + 1][x]
            updateQueue(x, y + 1, newDist)

        visited[f"{x},{y}"] = dist
        if x == xMax - 1 and y == yMax - 1:
            print(dist)

def extend():
    global input
    global xMax
    global yMax
    for y in range(yMax):
        for x in range((xMax * 5) - xMax):
            value = input[y][x] + 1
            if value > 9:
                value = 1
            input[y].append(value)
    for y in range((yMax * 5) - yMax):
        newLine = []
        for x in range(len(input[y])):
            value = input[y][x] + 1
            if value > 9:
                value = 1
            newLine.append(value)
        input.append(newLine)
    xMax = len(input[0])
    yMax = len(input)

def part1():
    #y, x, distance, visited
    heapq.heappush(queue,[0,0,0])
    performMagic()


def part2():
    extend()
    heapq.heappush(queue,[0,0,0])
    performMagic()

if __name__ == '__main__':
    parse()
    part2()