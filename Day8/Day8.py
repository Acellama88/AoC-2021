import re

file = "./Day8/input.txt"
finalAnswer = 0
input = []
s0 = []
s1 = []
s2 = []
s3 = []
s4 = []
s5 = []
s6 = []
s7 = []
s8 = []
s9 = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line)

def part1():
    vals = [2, 4, 3, 7]
    total = 0
    for output in input:
        valid = output.split(" | ")[1]
        tokens = valid.split()
        for val in vals:
            for token in tokens:
                if val == len(token):
                    total += 1
    print(total)

#0 (6) -> 8
#1 (2) -> 0, 3, 4, 7, 8, 9 - Unique
#2 (5) -> 8
#3 (5) -> 8, 9
#4 (4) -> 8, 9 - Unique
#5 (5) -> 6, 8, 9
#6 (6) -> 8
#7 (3) -> 0, 3, 8, 9 - Unique
#8 (7) -> Unique
#9 (6) -> 8

#1, #4, #7, and #8
#6 Does not include #1
#0 Does Not include #4
#9 includes #1
#3 includes #1
#5 in 6, 8, and 9
#2 remaining

def clear():
    s0.clear()
    s1.clear()
    s2.clear()
    s3.clear()
    s4.clear()
    s5.clear()
    s6.clear()
    s7.clear()
    s8.clear()
    s9.clear()

def findNum(Display):
    temp = sorted(Display)
    if s0 == temp:
        return 0
    if s1 == temp:
        return 1
    if s2 == temp:
        return 2
    if s3 == temp:
        return 3
    if s4 == temp:
        return 4
    if s5 == temp:
        return 5
    if s6 == temp:
        return 6
    if s7 == temp:
        return 7
    if s8 == temp:
        return 8
    if s9 == temp:
        return 9

def part2():
    total = 0
    for output in input:
        clear()
        answer = 0
        numbers = output.split(" | ")[0].split()
        display = output.split(" | ")[1].split()
        decode = [ -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        for i in range(len(numbers)):
            numbers[i] = "".join(sorted(numbers[i]))
            if len(numbers[i]) == 2:
                decode[i] = 1
                s1.extend(sorted(numbers[i]))
            if len(numbers[i]) == 4:
                decode[i] = 4
                s4.extend(sorted(numbers[i]))
            if len(numbers[i]) == 3:
                decode[i] = 7
                s7.extend(sorted(numbers[i]))
            if len(numbers[i]) == 7:
                decode[i] = 8
                s8.extend(sorted(numbers[i]))
        #find 6
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            if len(numbers[i]) == 6:
                temp = sorted(numbers[i])
                result = all(elem in temp for elem in s1)
                if not result:
                    decode[i] = 6
                    s6.extend(temp)
                    break
        #find 0
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            if len(numbers[i]) == 6:
                temp = sorted(numbers[i])
                result = all(elem in temp for elem in s4)
                if not result:
                    decode[i] = 0
                    s0.extend(temp)
                    break
        #find 9
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            if len(numbers[i]) == 6:
                decode[i] = 9
                s9.extend(sorted(numbers[i]))
                break
        #find 3
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            if len(numbers[i]) == 5:
                temp = sorted(numbers[i])
                result = all(elem in temp for elem in s1)
                if result:
                    decode[i] = 3
                    s3.extend(temp)
                    break
        #find 5
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            if len(numbers[i]) == 5:
                temp = sorted(numbers[i])
                result = all(elem in s6 for elem in temp)
                result = result and all(elem in s9 for elem in temp)
                if result:
                    decode[i] = 5
                    s5.extend(temp)
                    break
        #find 2
        for i in range(len(numbers)):
            if decode[i] != -1:
                continue
            decode[i] = 2
            s2.extend(sorted(numbers[i]))
            break
        for token in display:
            answer = (answer * 10) + findNum(token)
        total += answer    
    print(total)

if __name__ == '__main__':
    parse()
    part2()