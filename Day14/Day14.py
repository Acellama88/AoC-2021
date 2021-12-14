import re

file = "./Day14/input.txt"
finalTotal = 0
rules = {}
newRules = {}

#polymer = "NNCB"
polymer = "KFVHFSSVNCSNHCPCNPVO"

def parse():
    global rules
    with open(file) as f:
        for line in f:
            tokens = line.strip().split(" -> ")
            rules[tokens[0]] = tokens[1]

def part1():
    global polymer
    for i in range(10):
        newPoly = ""
        for j in range(len(polymer)):
            newPoly += polymer[j]
            if j == len(polymer) - 1:
                polymer = newPoly
                break
            pair = polymer[j:j+2]
            newPoly += rules[pair]
        print(polymer)
    polyList = list(polymer)
    cMax = max(polyList, key=polyList.count)
    cMin = min(polyList, key=polyList.count)

    print(polymer.count(cMax) - polymer.count(cMin))
    #print(polymer)

def convertDict():
    global rules
    for rule in rules:
        temp = rules[rule]
        temp = rule[0] + temp + rule[1]
        rules[rule]=temp

def part2():
    convertDict()
    global polymer
    for i in range(40):
        newPoly = ""
        j = 0
        maxCount = 0
        while j < len(polymer) - 1:
            count = 2
            while polymer[j:j+count] in rules and j+count <= len(polymer):
                count += 1
            if count > maxCount:
                maxCount = count
            temp = rules[polymer[j:j+count-1]]
            newPoly += temp[0:-1]
            j = j + count-2
        #add new pieces
        newPoly += polymer[-1]

        
        #k = 0
        #while k < len(polymer)-2:
        #    j =  k + 1
        #    while j - k < maxCount:
        #        diff = j - k
        #        temp = polymer[k:j+1]
        #        if temp in rules:
        #            j += 1
        #            continue
        #        temp2 = newPoly[k*2:j*2 +1]
        #        rules[temp] = temp2
        #        j += 1
        #    k += 1
        polymer = newPoly


if __name__ == '__main__':
    parse()
    part2()