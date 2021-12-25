import re

file = "./Day22/example.txt"
finalTotal = 0
input = []

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(list(filter(None,re.split(" |x|y|z|,|\.\.|=|\n",line))))
    for line in input:
        if int(line[1]) >= int(line[2]) or int(line[3]) >= int(line[4]) or int(line[5]) >= int(line[6]):
            print ("Oh No!")

def inRange(v1, v2, rMin, rMax):
    if rMin <= v1 < rMax or rMin < v2 <= rMax:
        return True
    return False


def checkCubes(c1: list, c2:list):
    #check X colision
    if not(inRange(c1[0], c1[1], c2[0], c2[1]) or inRange(c2[0], c2[1], c1[0], c1[1])):
        return False
    if not(inRange(c1[2], c1[3], c2[2], c2[3]) or inRange(c2[2], c2[3], c1[2], c1[3])):
        return False      
    if not(inRange(c1[4], c1[5], c2[4], c2[5]) or inRange(c2[4], c2[5], c1[4], c1[5])):
        return False
    return True

def part1():
    onLights = {}
    for line in input:
        xMin = int(line[1])
        xMax = int(line[2])
        yMin = int(line[3])
        yMax = int(line[4])
        zMin = int(line[5])
        zMax = int(line[6])
        if not(-50 <= xMin <= 50) or not(-50 <= yMin <= 50) or not(-50 <= zMin <= 50):
            continue
        for x in range(xMin,xMax + 1):
            for y in range(yMin,yMax + 1):
                for z in range(zMin,zMax + 1):
                    if line[0] == "on":
                        onLights[(x,y,z)] = True
                    else:
                        onLights.pop((x,y,z), None)
    print(len(onLights))

    # All X First
def collideCubes(c1: list, c2:list):
    leastX = min(c1[0], c2[0])
    leastY = min(c1[2], c2[2])
    leastZ = min(c1[4], c2[4])
    mostX = max(c1[1], c2[1])
    mostY = max(c1[3], c2[3])
    mostZ = max(c1[5], c2[5])
    midMinX = max(c1[0], c2[0])
    midMaxX = min(c1[1], c2[1])
    midMinY = max(c1[2], c2[2])
    midMaxY = min(c1[3], c2[3])
    midMinZ = max(c1[4], c2[4])
    midMaxZ = min(c1[5], c2[5])

    s1 = [leastX, c2[0],    leastY, c2[2],    leastZ, c2[4]]
    s2 = [midMinX, midMaxX, leastY, c2[2],    leastZ, c2[4]]
    s3 = [c2[1], mostX,     leastY, c2[2],    leastZ, c2[4]]
    s4 = [leastX, c2[0],    midMinY, midMaxY, leastZ, c2[4]]
    s5 = [midMinX, midMaxX, midMinY, midMaxY, leastZ, c2[4]]
    s6 = [c2[1], mostX,     midMinY, midMaxY, leastZ, c2[4]]
    s7 = [leastX, c2[0],    c2[3], mostY,     leastZ, c2[4]]
    s8 = [midMinX, midMaxX, c2[3], mostY,     leastZ, c2[4]]
    s9 = [c2[1], mostX,     c2[3], mostY,     leastZ, c2[4]]

    s10 = [leastX, c2[0],    leastY, c2[2],    midMinZ, midMaxZ]
    s11 = [midMinX, midMaxX, leastY, c2[2],    midMinZ, midMaxZ]
    s12 = [c2[1], mostX,     leastY, c2[2],    midMinZ, midMaxZ]
    s13 = [leastX, c2[0],    midMinY, midMaxY, midMinZ, midMaxZ]
    s14 = [midMinX, midMaxX, midMinY, midMaxY, midMinZ, midMaxZ] #Actual Colision Zone
    s15 = [c2[1], mostX,     midMinY, midMaxY, midMinZ, midMaxZ]
    s16 = [leastX, c2[0],    c2[3], mostY,     midMinZ, midMaxZ]
    s17 = [midMinX, midMaxX, c2[3], mostY,     midMinZ, midMaxZ]
    s18 = [c2[1], mostX,     c2[3], mostY,     midMinZ, midMaxZ]

    s19 = [leastX, c2[0],    leastY, c2[2],    c2[5], mostZ]
    s20 = [midMinX, midMaxX, leastY, c2[2],    c2[5], mostZ]
    s21 = [c2[1], mostX,     leastY, c2[2],    c2[5], mostZ]
    s22 = [leastX, c2[0],    midMinY, midMaxY, c2[5], mostZ]
    s23 = [midMinX, midMaxX, midMinY, midMaxY, c2[5], mostZ]
    s24 = [c2[1], mostX,     midMinY, midMaxY, c2[5], mostZ]
    s25 = [leastX, c2[0],    c2[3], mostY,     c2[5], mostZ]
    s26 = [midMinX, midMaxX, c2[3], mostY,     c2[5], mostZ]
    s27 = [c2[1], mostX,     c2[3], mostY,     c2[5], mostZ]

    allLists = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12, s13, s15, s16, s17, s18, s19, s20, s21, s22, s23, s24, s25, s26, s27]
    retList = []

    for sect in allLists:
        if sect[0] == sect[1] or sect[2] == sect[3] or sect[4] == sect[5]:
            continue
        retList.append(sect)
    return retList


def part2():
    onLights = {}
    total = 0
    for line in input:
        toPop = []
        toAdd = []
        xMin = int(line[1])
        xMax = int(line[2])
        yMin = int(line[3])
        yMax = int(line[4])
        zMin = int(line[5])
        zMax = int(line[6])
        for cube in onLights:
            cmd = [xMin,xMax,yMin,yMax,zMin,zMax]
            cb = onLights[cube]
            if checkCubes(cb,cmd):
                toPop.append(cube)
                newCubes = collideCubes(cb,cmd)
                toAdd.extend(newCubes)
        if line[0] == "on":
            toAdd.append([xMin,xMax,yMin,yMax,zMin,zMax])
        for pc in toPop:
            onLights.pop(pc, None)
        for nc in toAdd:
            onLights[(nc[0],nc[1],nc[2],nc[3],nc[4],nc[5])] = nc
    for cube in onLights:
        total += abs(cube[0] - cube[1]) * abs(cube[2] - cube[3]) * abs(cube[4] - cube[5])
    print(total)

if __name__ == '__main__':
    parse()
    retVal = []
    total = 0
    if checkCubes([0,5,0,5,0,5],[0,5,0,1,0,5]):
        retVal = collideCubes([0,5,0,5,0,5],[0,5,0,1,0,5])
    for cube in retVal:
        total += abs(cube[1] - cube[0]) * abs(cube[3] - cube[2]) * abs(cube[5] - cube[4])
    part2()