import re
import math

file = "./Day14/example.txt"
finalTotal = 0
rules = {}
newRules = {}

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
    print(polymer)

def part2():
    global polymer
    i = 0
    pairs = {}
    while i < len(polymer)-1:
        pairs[polymer[i] + polymer[i+1]] = 1
        i += 1
    for turn in range(0,40): #technically 39 since while above does 1st one...
        newPairs = {}
        for pair in pairs:
            newChar = rules[pair]
            if (pair[0] + newChar) in newPairs:
                newPairs[pair[0] + newChar] += pairs[pair]
            else:
                newPairs[pair[0] + newChar] = pairs[pair]
            if (newChar + pair[1]) in newPairs:
                newPairs[newChar + pair[1]] += pairs[pair]
            else:
                newPairs[newChar + pair[1]] = pairs[pair]
        pairs = newPairs.copy()
        length = 1
        for pair in pairs:
            length += pairs[pair]
    totals = {}
    for pair in pairs:
        for char in pair:
            if char in totals:
                totals[char] += pairs[pair]
            else:
                totals[char] = pairs[pair]
    for char in totals:
        totals[char] = math.ceil(totals[char]/2)
    max_key = max(totals,key=totals.get)
    min_key = min(totals,key=totals.get)
    print(totals[max_key] - totals[min_key])


if __name__ == '__main__':
    parse()
    part2()