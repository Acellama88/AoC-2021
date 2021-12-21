import re
import math

file = "./Day19/input.txt"


finalTotal = 0
input = []
scanners = {}
totalScanners = 0
locationScanners = []

def calcDistance(p1: list, p2:list):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    z = p1[2] - p2[2]
    vec = x ** 2 + y ** 2 + z ** 2
    vec = math.sqrt( vec )
    vec = round(vec,4)
    return vec

def parse():
    global scanners
    global totalScanners
    i = -1
    scanner = {}
    beacons = []
    with open(file) as f:
        for line in f:
            if len(line) < 3:
                scanner["beacons"] = beacons
                scanners[f"{i}"] = scanner
            elif line[0:3] == "---":
                beacons = []
                scanner = {}
                i += 1
            else:
                tokens = line.strip().split(",")
                beacons.append([int(tokens[0]),int(tokens[1]),int(tokens[2])])
        scanner["beacons"] = beacons
        scanners[f"{i}"] = scanner #final scanner added
    totalScanners = i + 1

def generateDistance(beacons:list):
    dists = []
    beac = []
    for b in range(len(beacons)):
        for d in range(len(beacons)):
            beac.append(calcDistance(beacons[b], beacons[d]))
        beac.sort()
        dists.append(beac)
        beac = []
    return dists

def compareDistances(b0:list, b1:list):
    x = 0
    y = 0
    count = 0
    while x < len(b0) and y < len(b1):
        if b0[x] == b1[y]:
            count += 1
            x += 1
            y += 1
        elif b0[x] < b1[y]:
            x += 1
        else:
            y += 1
    return count >= 12

def mergeScanners(s0, s1, l0, l1):
    global scanners
    global locationScanners
    scan0 = scanners[str(s0)]
    scan1 = scanners[str(s1)]

    b00 = scan0["beacons"][l0[0]]
    b01 = scan0["beacons"][l1[0]]

    b10 = scan1["beacons"][l0[1]]
    b11 = scan1["beacons"][l1[1]]

    dx0 = b00[0] - b01[0]
    dy0 = b00[1] - b01[1]
    dz0 = b00[2] - b01[2]

    dx1 = b10[0] - b11[0]
    dy1 = b10[1] - b11[1]
    dz1 = b10[2] - b11[2]

    retVal = [1,1,1]
    temp = [dx1, dy1, dz1]
    reorder = [0, 1, 2]

    if abs(dx0) != abs(temp[0]) and abs(dx0) == abs(temp[1]):
        dx1 = temp[1]
        reorder[0] = 1
    if abs(dx0) != abs(temp[0]) and abs(dx0) == abs(temp[2]):
        dx1 = temp[2]
        reorder[0] = 2
    if abs(dy0) != abs(temp[1]) and abs(dy0) == abs(temp[0]):
        dy1 = temp[0]
        reorder[1] = 0
    if abs(dy0) != abs(temp[1]) and abs(dy0) == abs(temp[2]):
        dy1 = temp[2]
        reorder[1] = 2
    if abs(dz0) != abs(temp[2]) and abs(dz0) == abs(temp[0]):
        dz1 = temp[0]
        reorder[2] = 0
    if abs(dz0) != abs(temp[2]) and abs(dz0) == abs(temp[1]):
        dz1 = temp[1]
        reorder[2] = 1

    if dx0 != dx1:
        retVal[0] = -1
    if dy0 != dy1:
        retVal[1] = -1
    if dz0 != dz1:
        retVal[2] = -1
    
    corScanner = [b00[0] - (retVal[0] * b10[reorder[0]]), b00[1] - (retVal[1] * b10[reorder[1]]), b00[2] - (retVal[2] * b10[reorder[2]])]
    #print(f"Scanner {str(s1)} - {corScanner}")
    locationScanners.append(corScanner)
    beacons = list(scan0["beacons"])
    for beacon in scan1["beacons"]:
        newCoor = [beacon[reorder[0]] * retVal[0] + corScanner[0], beacon[reorder[1]] * retVal[1] + corScanner[1], beacon[reorder[2]] * retVal[2] + corScanner[2]]
        if not(newCoor in beacons):
            beacons.append(newCoor)
    scanners.pop(str(s1))
    scan0["beacons"] = beacons
    scan0["distances"] = generateDistance(beacons)
    scanners[str(s0)] = scan0 #not needed but doing it anyways because python doesn't make any sense.\

def part1():
    #calculate all distances for each beacon
    for scan in scanners:
        beac = scanners[scan]["beacons"]
        dist = generateDistance(beac)
        scanners[scan]["distances"] = dist
    scanner0 = scanners["0"]
    while len(scanners) > 1: #while more scanners to match
        dists0 = scanner0["distances"]
        for i in range(1,totalScanners): #go through all total scanners
            if not f"{i}" in scanners: #if scanner already matched
                continue
            distsX = scanners[f"{i}"]["distances"] #get compare scanner distances
            loc0 = []
            loc1 = []
            loc = 0
            for a in range(len(dists0)): #for each beacon of scanner 0
                for b in range(len(distsX)): #for each beacon of scanner X
                    if compareDistances(dists0[a],distsX[b]):
                        #We Found a winner
                        if loc == 0:
                            loc0 = [a,b]
                            loc += 1
                            continue
                        else:
                            #don't use two points where X, Y, or Z point is the same.  Need a +/- differential on the points
                            if (scanner0["beacons"][a][0] == scanner0["beacons"][loc0[0]][0]) or (scanner0["beacons"][a][1] == scanner0["beacons"][loc0[0]][1]) or (scanner0["beacons"][a][2] == scanner0["beacons"][loc0[0]][2]):
                                continue
                            if (scanner0["beacons"][b][0] == scanner0["beacons"][loc0[1]][0]) or (scanner0["beacons"][b][1] == scanner0["beacons"][loc0[1]][1]) or (scanner0["beacons"][b][2] == scanner0["beacons"][loc0[1]][2]):
                                continue
                            loc1 = [a,b]
                            loc += 1
                            continue
                if loc > 1:
                    break
            if loc > 1:
                mergeScanners(0, i, loc0, loc1)
                break
    #print(len(scanners["0"]["beacons"]))

def part2():
    part1()
    maxDist = 0
    i = 0
    while i < len(locationScanners):
        j = i + 1
        while j < len(locationScanners):
            x = abs(locationScanners[i][0] - locationScanners[j][0])
            y = abs(locationScanners[i][1] - locationScanners[j][1])
            z = abs(locationScanners[i][2] - locationScanners[j][2])
            if (x + y + z) > maxDist:
                maxDist = x + y + z
            j += 1
        i += 1
    print(maxDist)

if __name__ == '__main__':
    parse()
    part2()