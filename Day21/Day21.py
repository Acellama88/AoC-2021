import re

solutions = {}

dice = 1
rolled = 0
spots = 10

turn = 0

s1 = 0
s2 = 0

p1 = 7 #actually 8, but doing 0 based for more ease
p2 = 8 #actually 9, but doing 0 based for more ease

def roll():
    global dice, rolled
    retVal = 0
    for i in range(3): #roll 3 times
        retVal += dice
        if dice == 100:
            dice = 1
        else:
            dice += 1
        rolled += 1 #track total rolled value
    return retVal

def part1():
    global p1, p2, s1, s2, turn
    while s1 < 1000 and s2 < 1000:
        die = roll() #get die roll
        if turn % 2 == 0: #determine turn
            p1 = (p1 + die) % spots #move
            s1 += p1 + 1 #add score
        else:
            p2 = (p2 + die) % spots #move
            s2 += p2 + 1 #add score
        turn += 1 #more turns!
    print(min([s1, s2]) * (rolled)) #final printout

def rollForIt(p1, p2, s1, s2):
    global solutions
    #Check Wins
    if (p1, p2, s1, s2) in solutions: #Can we Neo this?
        return solutions[(p1, p2, s1, s2)]
    if s1 >= 21: #Did I win?
        return [1, 0]
    if s2 >= 21: #Did they win?
        return [0, 1]
    #Not a Winner Yet - So lets calculate it!
    wins = [0,0]
    #3 rolls for each possible choice (1-3), Hip Hip Hurray!
    for a in range(1,4):
        for b in range(1,4):
            for c in range(1,4):
                #what is my new position for P1
                np1 = (p1+a+b+c)%10
                #new score for player 1
                ns1 = s1 + np1 + 1 #1 extra is needed because board location is 0 based, and puzzle wants 1 based
                #This controls whose turn it is! But don't forget it
                win = rollForIt(p2, np1, s2, ns1)
                #Store the wins
                wins[0] += win[1]
                wins[1] += win[0]
    #Now that we have a solution - lets save it because otherwise thats a lot of Bitcoin lost not mining
    solutions[(p1, p2, s1, s2)] = wins
    return wins #Return the results

def part2():
    global p1, p2
    results = rollForIt(p1, p2, 0, 0) #Zhu Li - Do the thing!
    print(results)

if __name__ == '__main__':
    part2()