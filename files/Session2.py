import datetime, time, math
def date():
    date = datetime.datetime.now()
    print(date.strftime("%j \n%A \n%Y %M"))
    time.sleep(1)
    main()

def poundConvert():
    print("GBP Converter £ -> ?")
    moneyIn = float(input("Enter your desired amount of GBP: "))
    moneyOut = moneyIn
    currencyChoice = input("Yen or Euros?\n1 - €\n2 - ¥\n")
    if currencyChoice == "1":
        moneyOut *=  1.26
        moneyStr = "€"+str(round(moneyOut,2))
    elif currencyChoice == "2":
        moneyOut *= 124.6
        moneyStr = "¥"+str(round(moneyOut,2))
    else:
        print("Error: You have selected an invalid option. Restarting...")
        poundConvert()

    if moneyStr[::-1].find(".") == 2: print("You have",moneyStr)
    else: print("You have",moneyStr+"0")

    time.sleep(1)
    main()

    

def holidayMoney():
    moneyCur = 500
    print("Italian Holiday\n\nYou have: €"+str(moneyCur),"\n\n")
    foodSpent = float(input("How much was spent on food?\n€"))
    tripsSpent = float(input("\nHow much was spent on trips?\n€"))
    presentsSpent = float(input("\nHow much was spent on presents?\n€"))

    moneyCur = round(moneyCur - (foodSpent + tripsSpent + presentsSpent),2)
    if str(moneyCur)[::-1].find('.') == 2: moneyStr = str(moneyCur)
    else: moneyStr = str(moneyCur)+"0"
    print("You have: €"+moneyStr+" left.")
    time.sleep(0.2)
    convertCheck = input("Would you like to covert to GBP?\ny - Yes")
    if convertCheck == 'y':
        moneyCur = round(moneyCur/1.26, 2)
        if str(moneyCur)[::-1].find('.') == 2: moneyStr = str(moneyCur)
        else: moneyStr = str(moneyCur)+"0"
        print("\n\n You have: £"+moneyStr+" left.")
    else:
        print("Invalid option.")

    time.sleep(1)
    main()

def cylinders():
    print("Cylinders (_()\n")
    p = math.pi
    r = float(input("Enter radius: "))
    h = float(input("\nEnter height: "))
    vol = p* pow(r,2)*h
    surfArea = 2*p*r*(r+h)
    print("\nVolume:",vol,"\nSurface Area",surfArea)

    time.sleep(1)
    main()
    
def main():
    options = [
        date,
        poundConvert,
        holidayMoney,
        cylinders
        ]
    print("\nOptions:")
    for i in range(len(options)):
        print(str(i+1)+" - "+options[i].__name__)
        
    choice = int(input('\n'))
    print('\n')
    options[choice-1]()

main()
