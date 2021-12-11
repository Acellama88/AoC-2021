import re

file = "./Day11/input.txt"
finalTotal = 0
octopi = []
xmin = 0
xmax = 0
ymin = 0
ymax = 0

def parse():
    global octopi
    global xmax
    global ymax
    with open(file) as f:
        for line in f:
            arr = []
            temp = line.strip()
            for pi in temp:
                arr.append([int(pi), False])
            octopi.append(arr)
    xmax = len(octopi[0])
    ymax = len(octopi)

def turn():
    check = True
    for line in octopi:
        for pi in line:
            check &= pi[1]
            if pi[1] == True:
                pi[0] = 1
                pi[1] = False
            else:
                pi[0] += 1
    return check

def flash():
    global xmin
    global xmax
    global ymin
    global ymax
    flashCount = 0
    for y in range(len(octopi)):
        for x in range(len(octopi[y])):
            if octopi[y][x][0] > 9 and not octopi[y][x][1]:
                if y > ymin and x > xmin: #top left
                    octopi[y-1][x-1][0] += 1
                if y > ymin: #top
                    octopi[y-1][x][0] += 1
                if y > ymin and x < xmax - 1: #top right
                    octopi[y-1][x+1][0] += 1
                if x < xmax - 1: #right
                    octopi[y][x+1][0] += 1
                if y < ymax - 1 and x < xmax - 1: #btm right
                    octopi[y+1][x+1][0] += 1
                if y < ymax - 1: #btm
                    octopi[y+1][x][0] += 1
                if y < ymax - 1 and x > xmin: #btm left
                    octopi[y+1][x-1][0] += 1
                if x > xmin: #left
                    octopi[y][x-1][0] += 1
                octopi[y][x][1] = True
                flashCount += 1
    return flashCount

def part1():
    global finalTotal
    for i in range(100):
        turn()
        done = False
        while not done:
            total = flash()
            finalTotal += total
            if total == 0:
                done = True
    print(finalTotal)

def part2():
    global finalTotal
    count = 0
    while True:
        count += 1
        if turn():
            break
        done = False
        while not done:
            total = flash()
            if total == 0:
                done = True
    print(count - 1)

if __name__ == '__main__':
    parse()
    part2()