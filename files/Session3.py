import time

def markCheck():
    mark = int(input("Please enter your exam mark: \n"))
    print("\n")
    if mark < 0 or mark >100:
        print("Invalid mark")
    elif mark >= 80:
        print("Distinction")
    elif mark >= 60:
        print("Merit")
    elif mark >= 40:
        print("Pass")
    else:
        print("A mark of", mark, "is a fail")

    time.sleep(1)
    main()

def oddEven():
    number = int(input("Enter a number\n"))
    print("\nYour number is even.\n" if number % 2 == 0 else "\nYour number is odd.\n") 
    time.sleep(1)
    main()

def greaterInteger():
    no1 = int(input('Enter an integer: '))
    no2 = int(input('Enter another integer: '))

    if no1 > no2:
        print(no1,'(integer A) is bigger.')
    elif no1 < no2:
        print(no2,'(integer B) is bigger.')
    else:
        print(no1,'(integer A) is equal to',no2,'(integer B)')
    
    time.sleep(1)
    main()

def login():
    validAccs = [['admin','deity'], ['user','mortal']]
    uidIn = input('\nEnter your user ID: ')
    pswdIn = input('Enter your password: ')
    if [uidIn, pswdIn] in validAccs:
        print('\nWelcome, '+uidIn+'.')
    else:
        print('\nIncorrect user ID or password.')
        time.sleep(1)
        login()
    
    time.sleep(1)
    main()

def loginAltered():
    validUids = ['admin','user']
    validPswds = ['deity','mortal']
    uidIn = input('\nEnter your user ID: ')

    if uidIn in validUids:
        i = validUids.index(uidIn)
        pswdIn = input('Enter your password: ')
        if pswdIn == validPswds[i]:
            
            print('\nWelcome, '+uidIn+'.')
        else:
            print('\nIncorrect password.')
            time.sleep(1)
            login()
    else:
        print('\nIncorrect user ID.')
        time.sleep(1)
        login()
    
    time.sleep(1)
    main()
def sportsMembership():
    price = 0
    memberType = ""
    age = int(input("How many years old are you? "))
    memberLength = int(input('How many years have you been a member? '))
    if age <= 18:
        price = 60 if memberLength < 2 else 40
        memberType = "Junior"
    elif age <= 49:
        price = 120 if memberLength < 10 else 90
        memberType = "Senior"
    else:
        price = 80 if memberLength < 10 else 50
        memberType = "Veteran"
    print("\nYou have the",memberType,"membership and must pay £"+str(price),'per year.')
    time.sleep(1)
    main()

def textbookDiscounts():
    bookCount = int(input("How many books do you wish to purchase? "))
    
    price = bookCount * 15
    discounts = ""
    if bookCount >= 20:
        price *= 0.9
        discounts = '10% off'
    elif bookCount >= 10:
        price *= 0.95
        discounts = '5% off'
    price += 5
    loyalCheck = input("\nAre you in the customer loyalty scheme?\ny - Yes\nn - No\n")
    if loyalCheck == 'y':
        price -= 5
        print("\nPostage is now free!\n")
        discounts = discounts + ', Free postage'
    print('SUMMARY\n-----------\nTOTAL: £'+str(price),'\nQUANITY:',bookCount,'\nDISCOUNTS:',discounts)
    time.sleep(1)
    main()
    

def main():
    options = [
        markCheck,
        oddEven,
        greaterInteger,
        login,
        loginAltered,
        sportsMembership,
        textbookDiscounts
        ]
    print("\nOptions:")
    for i in range(len(options)):
        print(str(i+1)+" - "+options[i].__name__)
        
    choice = int(input('\n'))
    print('\n')
    options[choice-1]()

main()
