import os, time, random,string 
playing = True
levelInt = 0
maxHits = 0
playerBoard = []
levels =[
    [
        ["A",(3,3),(7,3)],
        ["B",(1,2),(1,5)],
        ["C",(7,6),(9,6)],
        ["S",(5,7),(5,9)],
    ],
    [
        ["A",(0,5),(0,9)],
        ["B",(2,8),(5,8)],
        ["C",(9,1),(9,3)],
        ["S",(3,7),(5,7)],
    ],
    [
        ["A",(8,2),(8,6)],
        ["B",(3,4),(3,7)],
        ["C",(4,3),(4,5)],
        ["S",(5,4),(7,4)],
    ],
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

def createBoard():
    boardOut = [
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
    return boardOut
   
def isShipPosValid(boardIn, start, end):
    startCol, startRow = start
    endCol,endRow = end
    for row in range(startRow, endRow + 1):
        for col in range(startCol, endCol + 1):
            if not (row < 10) or not (col < 10) or boardIn[row][col] != "-":
                return False
    return True
def generateLevel():
    global level, turns, hits,levels, maxHits
    letters = list(string.ascii_uppercase)
    turns = 0
    maxHits = 0
    hits = 0
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

    
    genShip(level,5,"A")
    genShip(level,4,"B")
    genShip(level,3,"S")
    genShip(level,3,"C")
    drawBoard(level)
def placeShipChoice(length,char):
    global playerBoard
    os.system("cls")
    print("BUILD YOUR BOARD")
    drawBoardNoScoreBoard(playerBoard)
    print(f"Ship Letter: {char}\nShip Length: {length}")
    try:
        orientation = int(input("Enter orientation: 0 - Horizontal, 1 - Vertical"))
        x = int(input("Enter X value (0-9)"))
        y = int(input("Enter Y value (0-9)"))
        if orientation != 0 and orientation != 1:
            raise Exception("Invalid orientation")
    except:
        os.system("cls")
        print("Invalid input!")
        input()
        return placeShipChoice(length, char)

    success = placeShip(playerBoard, orientation, (x,y), length, char)
    if not success:
        os.system("cls")
        print("Invalid position!")
        input()
        return placeShipChoice(length, char)
    return success

        
    
def genShip(boardIn,length, char):
    success = False
    while not success:
        orientation = random.randint(0,1)
        startPos = (random.randint(0,9),random.randint(0,9))
        success = placeShip(boardIn,orientation, startPos, length, char)

def placeShip(boardIn,orientation, startPos, lengthIn, char):
    
    global maxHits
    length = lengthIn -1
    
    match orientation:
        case 0:
            endPos = (startPos[0]+length,startPos[1])
        case 1:
            endPos = (startPos[0],startPos[1]+length)
    test = [char, startPos, endPos]
    if isShipPosValid(boardIn,startPos,endPos):
            
        maxHits += (test[2][1]+1-test[1][1])*(test[2][0]+1-test[1][0])
        for y in range(test[1][1],test[2][1]+1):
            for x in range(test[1][0],test[2][0]+1):
                boardIn[y][x] = test[0]
        return True
    
    return False
def hasWon():
    global hits, maxHits
    if hits == maxHits:
        return True
    return False

def gameOver():
    global turns
    if turns == 30:
        return True
    return False

def drawBoard(board):
    global turns, hits, levelInt,maxHits
    print(f"Level {levelInt+1}")
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
    print(f"Turns: {turns}/30 Hits: {hits}/{maxHits}")

def drawBoardNoScoreBoard(board):
    global turns, hits, levelInt,maxHits
    #print(f"Level {levelInt+1}")
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

def setupLevel(levelInInt):
    global level, turns, hits,levels, maxHits
    turns = 0
    maxHits = 0
    levelIn = levels[levelInInt]
    hits = 0
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
        maxHits += (i[2][1]+1-i[1][1])*(i[2][0]+1-i[1][0])
        for y in range(i[1][1],i[2][1]+1):
            for x in range(i[1][0],i[2][0]+1):
                level[y][x] = i[0]

        
            
def playerTurn():
    global level, board, hits, turns,levelInt, choice
    

    column = input("Enter an X value (0-9): ")
    row = input("Enter a Y value (0-9): ")
    try:
        os.system("cls")
        row = int(row)
        column = int(column)
        if board[row][column] != "-":
            raise Exception("Already item here")
        if level[row][column] == "-":
            board[row][column] = "•"
        else:
            board[row][column] = "X"
            print("Hit!")
            hits += 1
        turns += 1
        if hasWon():
            os.system("cls")
            if choice == "1":
                if levelInt + 1 >= len(levels):
                    print("You win the game! Well done blud")
                    time.sleep(2)
                    playing = False
                    exit()
                else:
                    print("You win! Next level...")
                    levelInt += 1
                    time.sleep(2)
                    setupBoard()
                    setupLevel(levelInt)
            else:
                print("You win! Next level...")
                levelInt += 1
                time.sleep(2)
                setupBoard()
                generateLevel()
        elif gameOver():
            os.system("cls")
            print(f"Game Over! Final score: {levelInt}")
            time.sleep(2)
            playing = False
            exit()
        
            
    except:
        print("Invalid input!")
        drawBoard(board)
        playerTurn()
        return


def playerTurnVsAI():
    global level, board,playerBoard,hits
    os.system
    drawBothBoards(playerBoard, board)
    column = input("Enter an X value (0-9): ")
    row = input("Enter a Y value (0-9): ")
    try:
        os.system("cls")
        
        row = int(row)
        column = int(column)
        if board[row][column] != "-":
            raise Exception("Already item here")
        if level[row][column] == "-":
            board[row][column] = "•"
        else:
            board[row][column] = "X"
            print("You hit!")
            hits += 1
        if hasWon():
            os.system("cls")
            print("You win the game! Well done blud")
            time.sleep(2)
            playing = False
            exit()
        elif gameOver():
            os.system("cls")
            print(f"Game Over!")
            time.sleep(2)
            playing = False
            exit()
        
            
    except:
        print("Invalid input!")
        playerTurnVsAI()
        return



def drawBothBoards(board,board2):
    global turns, hits, levelInt,maxHits
    #print(f"Level {levelInt+1}")
    #First top upper Outline
    print("┌──", end="")
    for x in range(len(board[9])):    
        print(f"─┬──", end="")
    print("─┐", end="")

    #Second top upper Outline
    print("┌──", end="")
    for x in range(len(board[9])):    
        print(f"─┬──", end="")
    print("─┐")

    #First middle upper outline
    print("│  ", end="")
    
    for x in range(len(board[0])):
            
        print(f" │ {x}", end="")
    print(" │", end="")
    #Second middle upper outline
    print("│  ", end="")
    
    for x in range(len(board[0])):
            
        print(f" │ {x}", end="")
    print(" │")

    #First bottom upper outline
    
    print("├──",end="")

    for x in range(len(board[0])):
            
        print(f"─┼──", end="")
    print("─┤", end="")

    #Second bottom upper outline
    
    print("├──",end="")

    for x in range(len(board[0])):
            
        print(f"─┼──", end="")
    print("─┤")

    
    for y in range(len(board)-1):
        #First numbers
        print(f"│ {y}", end="")
        for x in range(len(board[y])):
            print(f" │ {board[y][x]}", end="")
        print(" │", end="")
        #Second numbers
        print(f"│ {y}", end="")
        for x in range(len(board2[y])):
            print(f" │ {board2[y][x]}", end="")
        print(" │")
        #First middle
        print("├──",end="")
        for x in range(len(board[y])):
            
            print(f"─┼──", end="")
        print("─┤", end="")
        #Second middle
        print("├──",end="")
        for x in range(len(board2[y])):
            
            print(f"─┼──", end="")
        print("─┤")

    #First bottom numbers
    print(f"│ 9", end="")
    for x in range(len(board[9])):
        print(f" │ {board[9][x]}", end="")
    print(" │", end="")
    #Second bottom numbers
    print(f"│ 9", end="")
    for x in range(len(board2[9])):
        print(f" │ {board2[9][x]}", end="")
    print(" │")
    #First bottom outline
    print("└──", end="")
    for x in range(len(board[9])):    
        print(f"─┴──", end="")
    print("─┘", end="")
    #Second bottom outline
    print("└──", end="")
    for x in range(len(board2[9])):    
        print(f"─┴──", end="")
    print("─┘")
  
def aiTurn():
    global playerBoard, level, board, aiHits, hits
    drawBothBoards(playerBoard, board)
    posToShoot = (random.randint(0,9),random.randint(0,9))
    hit = playerBoard[posToShoot[1]][posToShoot[0]]
    if hit == "X":
        aiTurn()
        return
    elif hit != "-":
        aiHits.append(posToShoot)
        playerBoard[posToShoot[1]][posToShoot[0]] = "X"
        aiHits += 1
    else:
        aiHits.append(posToShoot)
        playerBoard[posToShoot[1]][posToShoot[0]] = "•"
        
    
        

    
def createPlayerBoard():
    global playerBoard
    playerBoard = createBoard()
    placeShipChoice(5,"A")
    placeShipChoice(4,"B")
    placeShipChoice(3,"S")
    placeShipChoice(3,"C")
        
def start():
    global choice, playing, levelInt,board, level, aiHits,playerBoard
    os.system("cls")
    os.system("title SEABATTLE")
    print("Welcome to SEABATTLE!")    
    setupBoard()
    choice = input("Please select a gamemode:\n1: Campaign\n2: Endless\n3: Play AI\n")
    os.system("cls")
    if choice == "1":
        setupLevel(levelInt)
        
        
        while playing:
            drawBoard(board)
            playerTurn()
    elif choice == "2":
        
        generateLevel()
        while playing:
            drawBoard(board)
            playerTurn()
    elif choice == "3":
        createPlayerBoard()
        aiHits = []
        generateLevel()

        while playing:
            playerTurnVsAI()
            aiTurn()
        
    else:
        print("Incorrect input!")
        time.sleep(1)
        start()
        return      

start()

    
