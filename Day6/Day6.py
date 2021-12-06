import re
import numpy as np

file = "./Day6/input.txt"
input = []
coords = {}
totalCount = 0
fish = []

def parse():
    with open(file) as f:
        for line in f:
            input.extend(re.split(",",line.strip()))
            for i in input:
                fish.append(int(i))

def part1():
    for day in range(0,80):
        for i in range(len(fish)):
            fish[i] -= 1
            if fish[i] == -1:
                fish[i] = 6
                fish.append(8)
    print(len(fish))

def part2():
    schoolFish = [0,0,0,0,0,0,0,0,0]
    schoolFish[1] = fish.count(1)
    schoolFish[2] = fish.count(2)
    schoolFish[3] = fish.count(3)
    schoolFish[4] = fish.count(4)
    schoolFish[5] = fish.count(5)
    for count in range(0,256):
        newfish = schoolFish[0]
        schoolFish[0] = schoolFish[1]
        schoolFish[1] = schoolFish[2]
        schoolFish[2] = schoolFish[3]
        schoolFish[3] = schoolFish[4]
        schoolFish[4] = schoolFish[5]
        schoolFish[5] = schoolFish[6]
        schoolFish[6] = schoolFish[7]
        schoolFish[7] = schoolFish[8]
        schoolFish[8] = newfish
        schoolFish[6] += newfish
    totalCount = 0
    for i in range(0,9):
        totalCount += schoolFish[i]
    print(totalCount)

if __name__ == '__main__':
    parse()
    part2()