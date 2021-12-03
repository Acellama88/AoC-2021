input = "./Day3/input.txt"

def part1():
    data = []
    with open(input) as f:
        for line in f:
            data.append(line.strip())
    output  = []
    length = len(data[0])
    for i in range(0,length):
        output.append(0)
    for byte in data:
        for loc in range(0,length):
            if(byte[loc] == "1"):
                output[loc] += 1
    totalLen = len(data)
    gamma = 0
    epsilon = 0
    for loc in range(0,length):
        if(output[loc] >= totalLen/2):
            gamma |= (1 << length-loc-1)
        else:
            epsilon |= (1 << length-loc-1)
    print(f"Output = {gamma * epsilon}")    

def part2():
    data = []
    with open(input) as f:
        for line in f:
            data.append(line.strip())
    length = len(data[0])
    MSL = data
    LSL = data
    for loc in range(0,length):
        tMSL_1 = []
        tMSL_0 = []
        for byte in MSL:
            if(byte[loc] == '1'):
                tMSL_1.append(byte)
            else:
                tMSL_0.append(byte)
        if(len(tMSL_0) > len(tMSL_1)):
            MSL = tMSL_0
        else:
            MSL = tMSL_1
        if(len(MSL) == 1):
            break
    for loc in range(0,length):
        tLSL_1 = []
        tLSL_0 = []
        for byte in LSL:
            if(byte[loc] == '1'):
                tLSL_1.append(byte)
            else:
                tLSL_0.append(byte)
        if(len(tLSL_1) < len(tLSL_0)):
            LSL = tLSL_1
        else:
            LSL = tLSL_0
        if(len(LSL) == 1):
            break
    oxygen = 0
    co2 = 0
    for loc in range(0,length):
        if(MSL[0][loc] == '1'):
            oxygen |= (1 << length-loc-1)
        if(LSL[0][loc] == '1'):
            co2 |= (1 << length-loc-1)
    print(f"Total: {oxygen * co2}")

if __name__ == '__main__':
    part2()