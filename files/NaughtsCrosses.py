import os
gaming = True
grid = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]
def displayBoard():
    os.system("cls")
    for y in grid:
        print(' '.join(y))

def game():
    global gaming
    gaming = True
    player1 = Player("X","Player One")
    player2 = Player("O","Player Two")
    while gaming:
        
        player1.go(False)
        if gaming: player2.go(False)

    input()
def HasAnyoneWon():
    global grid
    if grid[0][0] != "-" and grid[0][0] == grid[1][1] == grid[2][2]:
        return grid[0][0]
    if grid[2][0] != "-" and grid[2][0] == grid[1][1] == grid[0][2]:
        return grid[2][0]
    for x in range(3):
        if grid[x][0] != "-" and grid[x][0] == grid[x][1] == grid[x][2]:
            return grid[x][0]
        if grid[0][x] != "-" and grid[0][x] == grid[1][x] == grid[2][x]:
            return grid[0][x]

    for row in grid:
        for col in row:
            if col == "-":
                return "NONE"

    return "DRAW"
            
        
    
    
        

class Player:
    def __init__(self, symbol, playerNo):
        self.symbol = symbol
        self.playerNo = playerNo
    def go(self,err):
        global gaming
        displayBoard()
        if err: print("\nYou input an invalid coordinate! Please try again:\n")
        else: print("\n"+str(self.playerNo)+"'s go:\n")
        row = input("Enter your row: ")
        column = input("Enter your column: ")
        try:
            row = int(row)-1
            column = int(column)-1
            if grid[row][column] == "-":
                grid[row][column] = self.symbol
            else:
                self.go(True)
            
        except:

            self.go(True)

        if HasAnyoneWon() == self.symbol:
            displayBoard()
            print("\n"+self.playerNo,"wins!")
            gaming = False
            return
        elif HasAnyoneWon() == "DRAW":
            displayBoard()
            print("\nIt's a draw!")
            gaming = False
            return
    
            
            

game()
