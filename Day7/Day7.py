import re

file = "./Day7/input.txt"
finalAnswer = 0
input = []
crabs = []

def parse():
    with open(file) as f:
        for line in f:
            input.extend(re.split(",",line.strip()))
            for i in input:
                crabs.append(int(i))

def part1():
    crabs.sort()
    min = crabs[0]
    max = crabs[len(crabs)-1]
    bestMove = 100000000000
    for i in range(min,max+1):
        curMoves = 0
        for crab in crabs:
            curMoves += abs(crab - i)
        if(curMoves < bestMove):
            bestMove = curMoves
    print(bestMove)

def countMove(count):
    total = 0
    if count % 2 == 0:
        #even
        total = (count / 2) * (count + 1)
    else:
        total = countMove(count - 1) + count
    return total

def part2():
    crabs.sort()
    min = crabs[0]
    max = crabs[len(crabs)-1]
    bestMove = 100000000000
    for i in range(min,max+1):
        curMoves = 0
        for crab in crabs:
            curMoves += countMove(abs(crab - i))
        if(curMoves < bestMove):
            bestMove = curMoves
    print(bestMove)

if __name__ == '__main__':
    parse()
    part2()