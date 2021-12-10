import re

file = "./Day10/input.txt"
finalTotal = 0
incomplete = []
input = []
openB = ['(','[','{','<']
closeB = [')',']','}','>']
score = [3, 57, 1197, 25137]
queue = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())
        

def checkClose(char):
    for bracket in closeB:
        if(char == bracket):
            return True
    return False    

def checkOpen(char):
    for bracket in openB:
        if(char == bracket):
            return True
    return False    

def addScore(char):
    global finalTotal
    for i in range(len(closeB)):
        if char == closeB[i]:
            finalTotal += score[i]
            return

def addScore2(closing: list):
    global incomplete
    score = 0
    for char in closing:
        score = (score * 5) + closeB.index(char) + 1
    incomplete.append(score)

def part1():
    global queue
    for line in input:
        if checkClose(line[0]):
            addScore(line[0])
            continue
        queue.append(line[0])
        for i in range(1, len(line)):
            if checkOpen(line[i]):
                queue.append(line[i])
            else:
                index = openB.index(queue[-1])
                if closeB[index] == line[i]:
                    queue.pop()
                else:
                    addScore(line[i])
                    break
        queue = []
    print(finalTotal)

def part2():
    global queue
    for line in input:
        skip = False
        if checkClose(line[0]):
            continue
        queue.append(line[0])
        for i in range(1, len(line)):
            if checkOpen(line[i]):
                queue.append(line[i])
            else:
                index = openB.index(queue[-1])
                if closeB[index] == line[i]:
                    queue.pop()
                else:
                    skip = True
                    break
        closeList = []
        if not skip:
            while len(queue) > 0:
                temp = queue.pop()
                closeList.append(closeB[openB.index(temp)])
            addScore2(closeList)
        queue = []
    incomplete.sort()
    print(incomplete[int(len(incomplete) / 2)])

if __name__ == '__main__':
    parse()
    part2()