import re

solutions = {}

dice = 1
rolled = 0
spots = 10

turn = 0

s1 = 0
s2 = 0

p1 = 7
p2 = 8

def roll():
    global dice, rolled
    retVal = 0
    for i in range(3):
        retVal += dice
        if dice == 100:
            dice = 1
        else:
            dice += 1
        rolled += 1
    return retVal

def part1():
    global p1, p2, s1, s2, turn
    while s1 < 1000 and s2 < 1000:
        die = roll()
        if turn % 2 == 0:
            p1 = (p1 + die) % spots
            s1 += p1 + 1
        else:
            p2 = (p2 + die) % spots
            s2 += p2 + 1
        turn += 1
    print(min([s1, s2]) * (rolled))

def rollForIt(p1, p2, s1, s2):
    global solutions
    #Check Wins
    if (p1, p2, s1, s2) in solutions:
        return solutions[(p1, p2, s1, s2)]
    if s1 >= 21:
        return [1, 0]
    if s2 >= 21:
        return [0, 1]
    #Not a Winner Yet - So lets calculate it!
    wins = [0,0]
    #3 rolls of each possible choice (1-3)
    for a in range(1,4):
        for b in range(1,4):
            for c in range(1,4):
                #what is my new position for P1
                np1 = (p1+a+b+c)%10
                #new score for player 1
                ns1 = s1 + np1 + 1
                #This controls whose turn it is! But don't forget it
                win = rollForIt(p2, np1, s2, ns1)
                #Store the wins
                wins[0] += win[1]
                wins[1] += win[0]
    #Now that we have a solution - lets save it because otherwise thats a lot of Bitcoin lost not mining
    solutions[(p1, p2, s1, s2)] = wins
    return wins

def part2():
    global p1, p2
    results = rollForIt(p1, p2, 0, 0)
    print(results)

if __name__ == '__main__':
    part2()