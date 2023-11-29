import os, random, math # Import various libraries
gaming = True # Define if the game is being played
grid = [ 
    [0,0,0],    
    [0,0,0],        # Intitialize the grid
    [0,0,0]
]


def displayBoard(): # Renders the board
    os.system("cls")
    gridVisual = [row[:] for row in grid]
    for x in range(len(grid)):
        for y in range(len(grid[0])): # Constructs a visual version of the grid
            if grid[x][y] == -1:      # e.g.
                ii = "X"              # -1 = "X", 1 = "O", 0 = "-"
            elif grid[x][y] == 0:
                ii = "-"
            else:
                ii = "O"
            gridVisual[x][y] = ii
    for i in gridVisual:
        print(' '.join(i))           # Prints the grid
def minimax(depth, player):  #Minimax algorithm to make the best move

    if player == 1:
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, +math.inf]

    if depth == 0 or not gaming:
        score = HasAnyoneWon()
        return [-1, -1, score]

    for cell in getEmptyValues():
        x, y = cell[0], cell[1]
        grid[x][y] = player
        score = minimax(depth - 1, -player)
        grid[x][y] = 0
        score[0], score[1] = x, y
        if player == 1:
            if score[2] > best[2]:
                best = score  # max value
        else:

            if score[2] < best[2]:
                best = score  # min value

    return best


def getEmptyValues():
    global grid
    emptyVals = []
    for x in range(3):
        for y in range(3):
            if grid[x][y] == 0: emptyVals.append([x,y])
    return emptyVals
            

def game():
    global gaming
    gaming = True
    player1 = Player("X","Player")
    player2 = AI("O","X","AI")

    while gaming:
        player1.go(False)
        if gaming: player2.go(False)
        
        

    input()
def HasAnyoneWon():
    global grid
    if grid[0][0] != 0 and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[2][0] != 0 and grid[2][0] == grid[1][1] == grid[0][2]:
        return grid[2][0]
    for x in range(3):
        if grid[x][0] != 0 and grid[x][0] == grid[x][1] == grid[x][2]:
            return grid[x][0]
        if grid[0][x] != 0 and grid[0][x] == grid[1][x] == grid[2][x]:
            return grid[0][x]

    for row in grid:
        for col in row:
            if col == 0:
                return -2

    return 0
            
        
class AI:
    def __init__(self, symbol, plySymbol,playerNo):
        self.symbol = symbol
        self.playerNo = playerNo
        self.plySymbol = plySymbol
    def go(self,err):
        global grid
        global gaming

        depth = len(getEmptyValues())

        if depth == 0 or not gaming:
            return


        displayBoard()
        if depth == 9:
            x = random([0, 1, 2])
            y = random([0, 1, 2])
        else:
            move = minimax(depth, 1)
            x, y = move[0], move[1]

        grid[x][y] = 1

        if HasAnyoneWon() == 1:
            displayBoard()
            print("\n"+self.playerNo,"wins!")
            gaming = False
            return
        elif HasAnyoneWon() == 0:
            displayBoard()
            print("\nIt's a draw!")
            gaming = False
            return
        
    
        

class Player:
    def __init__(self, symbol, playerNo):
        self.symbol = symbol
        self.playerNo = playerNo
    def go(self,err):
        global gaming, playerRow, playerCol
        displayBoard()
        if err: print("\nYou input an invalid coordinate! Please try again:\n")
        else: print("\n"+str(self.playerNo)+"'s go:\n")
        row = input("Enter your row: ")
        column = input("Enter your column: ")
        try:
            row = int(row)-1
            column = int(column)-1
            playerCol = column
            playerRow = row
            if grid[row][column] == 0:
                grid[row][column] = -1
            else:
                self.go(True)
            
        except:

            self.go(True)

        if HasAnyoneWon() == -1:
            displayBoard()
            print("\n"+self.playerNo,"wins!")
            gaming = False
            return
        elif HasAnyoneWon() == 0:
            displayBoard()
            print("\nIt's a draw!")
            gaming = False
            return
    
            
            

game()
