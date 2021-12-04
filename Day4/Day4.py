file = "./Day4/input.txt"
input = []
calledNumbers = []
bingoBoards = []
winner = []
winNum = 0
toRemove = []

def parse():
    with open(file) as f:
        for line in f:
            input.append(line.strip())
        calledNumbers.extend(str(input[0]).split(","))
        for i in range(2, len(input), 6):
            board = []
            for j in range(0,5):
                row = []
                tokens = str(input[i+j]).split(None)
                for k in range(0,5):
                    row.append(int(tokens[k]))
                board.append(row)
            bingoBoards.append(board)

def checkBoard(Board: list, number):
    for line in range(len(Board)):
        for num in range(0,5):
            if Board[line][num] == number:
                Board[line][num] = -1
                return checkWin(Board)

def checkWin(Board: list):
    #Check Horizontal
    for line in Board:
        if (line[0] + line[1] + line[2] + line[3] + line[4]) == -5:
            #Winner Winner Chicken Dinner
            winner.extend(Board)
            return True
    #Check Vertical
    for i in range(0,5):
        if (Board[0][i] + Board[1][i] + Board[2][i] + Board[3][i] + Board[4][i]) == -5:
            #Winner Winner Chicken Dinner
            winner.extend(Board)
            return True

def part1():
    win = False
    for call in calledNumbers:
        for board in bingoBoards:
            if(checkBoard(board, int(call))):
                #winner
                win = True
                winNum = int(call)
                break
        if win:
            break
    #Win Game
    finalTotal = 0
    for line in winner:
        for num in line:
            if(num != -1):
                finalTotal += num
    print(f"Answer: {finalTotal * winNum}")


def checkBoard2(Board: list, number):
    for line in range(len(Board)):
        for num in range(0,5):
            if Board[line][num] == number:
                Board[line][num] = -1
                return checkWin2(Board)

def checkWin2(Board: list):
    #Check Horizontal
    for line in Board:
        if (line[0] + line[1] + line[2] + line[3] + line[4]) == -5:
            #Winner Winner Chicken Dinner
            return True
    #Check Vertical
    for i in range(0,5):
        if (Board[0][i] + Board[1][i] + Board[2][i] + Board[3][i] + Board[4][i]) == -5:
            #Winner Winner Chicken Dinner
            return True
    

def part2():
    win = False
    for call in calledNumbers:
        toRemove = []
        for board in bingoBoards:
            if(checkBoard2(board, int(call))):
                if len(bingoBoards) == 1:
                    winner.extend(bingoBoards[0])
                    winNum = call
                    win = True
                    break
                else:
                    toRemove.append(board)
        if win:
            break
        else:
            for board in toRemove:
                bingoBoards.remove(board)
    #Win Game
    finalTotal = 0
    for line in winner:
        for num in line:
            if(num != -1):
                finalTotal += num
    print(f"Answer: {finalTotal * int(winNum)}")
    

if __name__ == '__main__':
    parse()
    part2()