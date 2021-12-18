import re

file = "./Day18/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())

def add(left, right):
    newNum = f"[{left},{right}]"
    return newNum

def checkNested(number: str):
    bracket = 0
    for i in range(len(number)):
        if number[i] == '[':
            bracket += 1
        elif number[i] == ']':
            bracket -= 1
        if bracket > 4:
            return True
    return False

def explode(number: str):
    result = ""
    bracket = 0
    i = 0
    while True:
        if number[i] == '[':
            bracket += 1
        elif number[i] == ']':
            bracket -= 1
        if bracket > 4 and number[i+1] != '[': #Boom Boom!
            #get both numbers
            start = i
            end = number.find("]", start)
            tokens = list(filter(None,re.split("\[|,|\]",number[start:end+1])))

            left = int(tokens[0])
            right = int(tokens[1])

            #add left leftwards if possible
            anyNum = re.findall("[0-9]",number[0:start])
            if len(anyNum) > 0:
                    #find first number, and add it
                    searching = True
                    LEDigit = -1
                    LSDigit = -1
                    loc = start
                    while searching:
                        loc -= 1
                        if number[loc] >= '0' and number[loc] <= '9':
                            if(LEDigit < 0):
                                #found end of some number
                                LEDigit = loc
                            if number[loc - 1] < '0' or number[loc - 1] > '9':
                                searching = False
                                LSDigit = loc
                    newLeft = int(number[LSDigit:LEDigit + 1]) + left
                    result += number[0:LSDigit] + str(newLeft) + number[LEDigit + 1:start] + '0' #put current spot as 0 as well!
            else:
                result += number[0:start] + '0'
                        
            #add right rightwards if possible
            anyNum = re.findall("[0-9]",number[end+1:])
            if len(anyNum) > 0:
                    #find first number, and add it
                    searching = True
                    REDigit = -1
                    RSDigit = -1
                    loc = end + 1
                    while searching:
                        loc += 1
                        if number[loc] >= '0' and number[loc] <= '9':
                            if(RSDigit < 0):
                                #found start of some number
                                RSDigit = loc
                            if number[loc + 1] < '0' or number[loc + 1] > '9':
                                searching = False
                                REDigit = loc
                    newRight = int(number[RSDigit:REDigit + 1]) + right
                    result += number[end+1:RSDigit] + str(newRight) + number[REDigit + 1:]
            else:
                result += number[end+1:]
            break
        i += 1
    return result

def split(number: str):
    retVal = ""
    tokens = list(filter(None,re.split("\[|,|\]",number)))
    value = ""
    for i in range(len(tokens)):
        if int(tokens[i]) >= 10:
            value = tokens[i]
            break
    start = number.find(value)
    end = start + len(value)
    left = int(int(value) / 2)
    right= int(float(value) / 2 + 0.5)
    retVal = number[0:start] + "[" + str(left) + ","  + str(right) + "]" + number[end:]
    return retVal

def checkSplits(number: str):
    tokens = list(filter(None,re.split("\[|,|\]",number)))
    for i in range(len(tokens)):
        if int(tokens[i]) >= 10:
            return True
    return False

def reduce(number: str):
    wip = number
    anyChange = True
    while anyChange:
        anyChange = False
        if checkNested(wip):
            anyChange = True
            wip = explode(wip)
        elif checkSplits(wip):
            anyChange = True
            wip = split(wip)
    return wip

def calcMagnitude(number:str):
    wip = number
    result = ""
    bracket = 0
    i = 0
    while True:
        if wip.find("[") < 0:
            break
        if wip[i+1] != '[':
            #get both numbers
            start = i
            end = wip.find("]", start)
            
            #check if any other numbers are in this range
            temp = wip[start+1:end].find("[")
            if temp > -1:
                i = temp + start + 1
                continue

            tokens = list(filter(None,re.split("\[|,|\]",wip[start:end+1])))

            left = int(tokens[0])
            right = int(tokens[1])

            newVal = left * 3 + right * 2
            result += wip[0:start] + str(newVal) + wip[end+1:] #put current spot as 0 as well!
            wip = result
            result = ""
            i = -1
        i += 1
    return int(wip)

def part1():
    val = input[0]
    for i in range(1, len(input)):
        val = add(val,input[i])
        val = reduce(val)
    print(calcMagnitude(val))

def part2():
    maxMag = 0
    for i in range(len(input)):
        for j in range(len(input)):
            if i == j:
                continue
            val = add(input[i],input[j])
            val = reduce(val)
            val = calcMagnitude(val)
            if(maxMag < val):
                maxMag = val
    print(maxMag)

if __name__ == '__main__':
    parse()
    part2()