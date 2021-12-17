import re

file = "./Day16/input.txt"
finalTotal = 0
input = []
message = ""

msgLen = 3
idLen = 3
litPack = 5
lenBits = 15
lenPac = 11


def parse():
    global message
    binary = []
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())
    for i in range(0,len(input[0]),2):
        binary.extend(bin(int(input[0][i:i+2], 16))[2:].zfill(8))
    message = "".join(binary)

def processResults(values, id):
    retVal = 0
    if id == 0: #add
        for val in values:
            retVal += val
    if id == 1: #product
        retVal = 1
        for val in values:
            retVal *= val
    if id == 2: #minimum
        retVal = min(values)
    if id == 3: #maximum
        retVal = max(values)
    if id == 5: #greater than
        if values[0] > values[1]:
            retVal = 1
    if id == 6: #less than
        if values[0] < values[1]:
            retVal = 1
    if id == 7: #equal to
        if values[0] == values[1]:
            retVal = 1
    return retVal

def extractLiteral(loc):
    global message
    val = 0
    litLoc = loc
    while True:
        temp = message[litLoc: litLoc + litPack]
        val = (val << 4) | int(temp[1:5],2)
        litLoc += 5
        if temp[0] == "0":
            break
    return [litLoc,val]

def extractLenSubPac(loc, id):
    global message
    values = []
    subLoc = loc
    length = int(message[subLoc: subLoc + lenBits],2)
    subLoc += lenBits
    endLoc = subLoc + length
    while subLoc < endLoc:
        temp = extractPacket(subLoc)
        subLoc = temp[0]
        values.append(temp[1])
    if subLoc != endLoc:
        print("Error!")
    retVal = processResults(values, id)
    return [subLoc, retVal]

def extractNumPac(loc, id):
    global message
    values = []
    subLoc = loc
    length = int(message[subLoc: subLoc + lenPac],2)
    subLoc += lenPac
    packCount = 0
    while packCount < length:
        temp = extractPacket(subLoc) 
        subLoc = temp[0]
        values.append(temp[1])
        packCount += 1
    retVal = processResults(values, id)
    return [subLoc, retVal]

def extractPacket(loc):
    global finalTotal
    global message
    value = 0
    pacLoc = loc
    version = message[pacLoc: pacLoc + msgLen] #for part 1
    finalTotal += int(version,2)
    pacLoc += msgLen
    id = int(message[pacLoc: pacLoc + idLen],2)
    pacLoc += idLen
    if id == 4:
        temp = extractLiteral(pacLoc)
        pacLoc = temp[0]
        value = temp[1]
    else:
        lenType = message[pacLoc: pacLoc + 1]
        pacLoc += 1
        if lenType == "0":
            temp = extractLenSubPac(pacLoc, id)
            pacLoc = temp[0]
            value = temp[1]
        else:
            temp = extractNumPac(pacLoc, id)
            pacLoc = temp[0]
            value = temp[1]
    return [pacLoc, value]

def part1():
    global finalTotal
    extractPacket(0)
    print(finalTotal)

def part2():
    global finalTotal
    temp = extractPacket(0)
    print(temp[1])

if __name__ == '__main__':
    parse()
    part2()

#110100101111111000101000
#VVVTTTAAAAABBBBBCCCCC

#V = Version
#T = ID (4)
#A = Literal (LS 4-bits)
#B = Literal (LS 4-bits)
#C = Literal (LS 4-bits)


#ID4 - Literal with 5 bit packets, MSB signals more data (1) or done (0)