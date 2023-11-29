import time

def countTo100():
    for count in range(1,101):
        print(count)
    time.sleep(1)
    main()


def tenTab():
    for i in range(1,101):
        print(('\t'+str(i)) if i % 10 == 0 else str(i))
    time.sleep(1)
    main()







def timesTable():
    for i in range(1,11):
        print(i,'* 12 =',str(i*12))
    
    time.sleep(1)
    main()

def timesTableGrid():
    for y in range(1,11):
        for x in range(1,11):
            print(str(x*y), end='\t')
        print('\n',end='')

    time.sleep(1)
    main()





def main():
    options = [
        countTo100,
        tenTab,
        timesTable,
        timesTableGrid
        ]
    print("\nOptions:")
    for i in range(len(options)):
        print(str(i+1)+" - "+options[i].__name__)
        
    choice = int(input('\n'))
    print('\n')
    options[choice-1]()

main()
