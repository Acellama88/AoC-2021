import re

file = "./Day19/input.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())

def part1():
    print("")

def part2():
    print("")

if __name__ == '__main__':
    parse()
    part1()