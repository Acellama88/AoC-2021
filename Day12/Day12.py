import re

file = "./Day12/input.txt"
output = []
input = []
nodes = {}

def parse():
    with open(file) as f:
        for line in f:
            if False:
                input.extend(re.split("",line.strip()))
            else:
                input.append(line.strip())
    for line in input:
        tokens = line.split("-")
        if tokens[0] in nodes:
            #append node?
            temp = nodes[tokens[0]]
            temp.append(tokens[1])
            nodes[tokens[0]] = temp
        else:
            #add node?
            nodes[tokens[0]] = [tokens[1]]
        if tokens[1] in nodes:
            #append node?
            temp = nodes[tokens[1]]
            temp.append(tokens[0])
            nodes[tokens[1]] = temp
        else:
            #add node?
            nodes[tokens[1]] = [tokens[0]]

def isLower(char):
    if char >= 'a' and char <= 'z':
        return True
    return False

def doPath(curPath: str, curNode):
    connections = nodes[curNode]
    for conNode in connections:
        if conNode == "end" or conNode == "start":
            continue
        elif isLower(conNode[0]) and curPath.find(conNode) < 0:
            #Have not processed this small node.
            doPath(curPath + "-" + curNode, conNode)
        elif not isLower(conNode[0]):
            #Big Cave
            doPath(curPath + "-" + curNode, conNode)
    if "end" in connections:
        output.append(curPath + "-end")

def doPath2(curPath: str, curNode):
    connections = nodes[curNode]
    for conNode in connections:
        if conNode == "end" or conNode == "start":
            continue
        elif isLower(conNode[0]) and curPath[0:6] == "-start" and curPath.find(conNode) >= 0:
            #Have not processed this small node.
            doPath2(curNode + curPath + "-" + curNode, conNode)
        elif isLower(conNode[0]) and curPath.find(conNode) < 0:
            #Have not processed this small node.
            doPath2(curPath + "-" + curNode, conNode)
        elif not isLower(conNode[0]):
            #Big Cave
            doPath2(curPath + "-" + curNode, conNode)
    if "end" in connections:
        output.append(curPath + "-end")
            

def part1():
    doPath("","start")
    print(len(output))

def part2():
    doPath2("","start")
    print(len(output))

if __name__ == '__main__':
    parse()
    part2()