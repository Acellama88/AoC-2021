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
        for j in range(len(polymer)): #change - needs to just increment
            found = True
            while found: #keep looping as we find keys
                count = 3
                temp = polymer[j:j+count]
                newPoly += polymer[j]
                if j == len(polymer) - 1:
                    polymer = newPoly
                    break
                pair = polymer[j:j+2]
                newPoly += rules[pair] #save largest subset, start at next letter
    polyList = list(polymer)
    cMax = max(polyList, key=polyList.count)
    cMin = min(polyList, key=polyList.count)

    print(polymer.count(cMax) - polymer.count(cMin))
    #print(polymer)

if __name__ == '__main__':
    parse()
    part2()