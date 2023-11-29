import time,random


def numberTotal():
    numbers = []
    curInput = 0
    while curInput != -1:
        curInput = int(input("Enter a number. Enter -1 to finish entering\z"))
        if curInput != -1: numbers.append(curInput)
    
    print("\nSum:",sum(numbers))
    time.sleep(1)
    main()

def minMax():
    numbers = []
    curInput = 0
    while curInput != -1:
        curInput = int(input("Enter a number. Enter -1 to finish entering\n"))
        if curInput != -1: numbers.append(curInput)
    numbers.sort()
    print("\nMax:",numbers[len(numbers)-1],"\nMin:",numbers[0])
    time.sleep(1)
    main()

def passChecking():
    
    password = ""
    while password != "password":
        password = input("Enter password: ")
        if password != "password":
            print("Incorrect password, try again....")
        
    print("** Login Successful")
    
    time.sleep(1)
    main()

def passCheckingWithLockout():
    attempts = 0
    password = ""
    while password != "password" and attempts < 3:
        password = input("Enter password: ")
        if password != "password":
            
            attempts += 1
            if attempts < 3: print("Incorrect password, try again....")
            else: print("Locked Out")
            
    if attempts < 3: print("** Login Successful")
    
    time.sleep(1)
    main()


def guessingGame():
    numberToGuess = int(input("Player A enter your chosen number "))
    while numberToGuess <= 1 or numberToGuess > 10:
        numberToGuess = int(input("Not a valid choice, please enter another number "))
    numberOfGuesses = 0
    guess = 0
    while guess != numberToGuess and numberOfGuesses < 5:
        guess = int(input("Player B have a guess "))
        numberOfGuesses += 1
    if guess == numberToGuess:
        print("Player B wins")
    else:
        print("Player A wins")

    time.sleep(1)
    main()


def guessingGameOnePlayer():
    numberToGuess = random.randint(1,100)
    numberOfGuesses = 0
    guess = 0
    while guess != numberToGuess:

        guess = int(input("\nHave a guess\n"))
        numberOfGuesses += 1
        if guess < numberToGuess: print("\nToo low")
        if guess > numberToGuess: print("\nToo high")
    if guess == numberToGuess:
        print("\nHuman wins! Guesses required:",numberOfGuesses)

    time.sleep(1)
    main()

    



def main():
    options = [
        numberTotal,
        minMax,
        passChecking,
        passCheckingWithLockout,
        guessingGame,
        guessingGameOnePlayer
        ]
    print("\nOptions:")
    for i in range(len(options)):
        print(str(i+1)+" - "+options[i].__name__)
        
    choice = int(input('\n'))
    print('\n')
    options[choice-1]()

main()
