import re

file = "./Day6/input.txt"
input = []
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
    for i in range(0,9):
        schoolFish[i] = fish.count(i)
    for count in range(0,256):
        newfish = schoolFish[0]
        for i in range(0,8):
            schoolFish[i] = schoolFish[i+1]
        schoolFish[8] = newfish
        schoolFish[6] += newfish
    totalCount = 0
    for i in range(0,9):
        totalCount += schoolFish[i]
    print(totalCount)

if __name__ == '__main__':
    parse()
    part2()