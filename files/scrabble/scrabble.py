import time, enchant, random, os
check = enchant.Dict("en_GB")
p1name = ""
p2name = ""
p1points = 0
p2points = 0
def main():
    choice = int(input("""SCRABBLE
Enter 1 to get the value of a scrabble letter
Enter 2 to get the value of a scrabble word
Enter 3 to play a game (incomplete)
Enter 4 to quit
"""))
    os.system("cls")
    if choice < 1 or choice > 4:
        print("Invalid choice")
        main()
        return
    else:
        if choice == 1:
            
            letter = input("Enter a letter: ").lower()
            value = GetLetterValue(letter)
            print("Letter",letter,"is worth",value,"points.")
            time.sleep(1)
            main()
            return
        elif choice == 2:
            word = input("Enter a word: ").lower()
            points = GetWordValue(word)
            print("Word",word,"is worth",points,"points.")
            time.sleep(1)
            main()
            return
        elif choice ==3:
            PlayTheGame()
        else:
            quit()

def DrawPoints(pointsOverload1, pointsOverload2):
    global p1points, p2points, p2name, p1name
    os.system("cls")
    print("""
---------------------
| %s's points: %s   |
---------------------
| %s's points: %s   |
---------------------""" % (p1name, p1points + pointsOverload1, p2name, p2points + pointsOverload2))

def PlayTheGame():
    global p1points, p2points, p2name, p1name
    p1points = 0
    p2points = 0

    p1name = input("Player 1's name: ")
    os.system("cls")
    p2name = input("Player 2's name: ")
    os.system("cls")
    for i in range(3):
        DrawPoints(0,0)
        p1points += DoAGo(p1name)
        DrawPoints(0,0)
        p2points += DoAGo(p2name)
    os.system("cls")
    finish = ""
    if p1points == p2points:
        finish = "It's a tie."
    else :
        finish = "%s wins!" % (p2name if p2points > p1points else p1name)
    print("""
---------------------
| %s         |
---------------------
""" % finish)
    time.sleep(1)
    main()
    return

def DoAGo(playerNo):

    letters = GetRandomLetters()
    pointsTemp = 0
    lettersAlreadyUsed = [False,False,False,False,False,False,False]
    print("\n\n%s's go." %  playerNo)
    print("\nYour letters:", "".join(letters).upper())
    word = input("\nEnter your word:\n")
    for i in range(len(word)):

        if not word[i] in letters:
            
            DrawPoints(0,0)
            print(word[i])
            print(letters)
            print("""\n
----------------------------
|No points. Invalid letter.|
----------------------------
""")
            time.sleep(1)
            return 0
        elif lettersAlreadyUsed[letters.index(word[i])] == True:
            DrawPoints(0,0)
            print("""\n
----------------------------------------
|No points. Letter used more than once.|
----------------------------------------
""")
            time.sleep(1)
            return 0
        elif not check.check(word):
            DrawPoints(0,0)
            print("""\n
-----------------------------
|No points. Not a real word.|
-----------------------------
""")
            time.sleep(1)
            return 0
        else:
            pointsTemp += GetLetterValue(word[i])
            
            lettersAlreadyUsed[letters.index(word[i])] = True
            if playerNo == p1name:
                DrawPoints(pointsTemp,0)
            else:
                DrawPoints(0,pointsTemp)
    print("""\n
-----------------------------------------
|Total points for that word: %s|
-----------------------------------------
""" % pointsTemp)
    time.sleep(1)
    return pointsTemp
            
    
def GetWordValue(word):
    points = 0
    if check.check(word):
       
        for i in word:
            points += GetLetterValue(i)
        return points
    else:
        print("Invalid word")
        return 0
    
def GetLetterValue(let):
    match let:
        case 'a' | 'e' | 'i' | 'o' | 'u' | 'l' | 'n' | 'r' | 's' | 't':
            return 1
        case 'd' | 'g':
            return 2
        case 'b'| 'c'| 'm'| 'p':
            return 3
        case 'f' | 'h'| 'v' | 'w' | 'y':
            return 4
        case 'k':
            return 5
        case 'j' | 'x':
            return 8
        case 'q' | 'z':
            return 10
def GetRandomLetters():
    letters = []
    sample = "qwertyuiopasdfghjklzxcvbnm"
    letters = random.sample(sample,7)

    return letters
if __name__ == "__main__":
    main()
