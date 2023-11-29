levels =[
    [
        ["A",(1,2),(1,5)],
        ["B",(3,3),(7,3)],
        ["B",(0,4),(2,4)],
        ["B",(0,4),(2,4)],
    ]
]
def setupBoard():
    global board
    board = [
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
    ]




def drawBoard(board):
    
    if board == None:
        return
    print("┌──", end="")
    for x in range(len(board[9])):    
        print(f"─┬──", end="")
    print("─┐")
    print("│  ", end="")
    for x in range(len(board[0])):
            
        print(f" │ {x}", end="")
    print(" │")
    print("├──",end="")
    for x in range(len(board[0])):
            
        print(f"─┼──", end="")
    print("─┤")
    
    for y in range(len(board)-1):
        print(f"│ {y}", end="")
        for x in range(len(board[y])):
            print(f" │ {board[y][x]}", end="")
        print(" │")
        print("├──",end="")
        for x in range(len(board[y])):
            
            print(f"─┼──", end="")
        print("─┤")

    print(f"│ 9", end="")
    for x in range(len(board[9])):
        print(f" │ {board[9][x]}", end="")
    print(" │")
    print("└──", end="")
    for x in range(len(board[9])):    
        print(f"─┴──", end="")
    print("─┘")

def setupLevel(levelIn):
    global level
    level = [
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
        ["-","-","-","-","-","-","-","-","-","-",],
    ]
    for i in levelIn:
        for y in range(i[1][1],i[2][1]+1):
            for x in range(i[1][0],i[2][0]+1):
                level[y][x] = i[0]

        
            
def playerTurn():
    global level, board
    drawBoard(board)
    row = input("Enter a row (0-9): ")
    column = input("Enter a column (0-9): ")
    try:
        row = int(row)
        column = int(column)
        if level[row][column] == "-":
            board[row][column] = "•"
        else:
            board[row][column] = "x"
    except:
        print("Invalid input!")
        playerTurn()
        return
    
setupBoard()

setupLevel(levels[0])

while True: playerTurn()

    
