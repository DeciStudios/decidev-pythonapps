def main():
    myArray = ["Tim","Nigel","Steve","Maggie"]
    newPerson = ""
    
    while True:
        choice = getUserChoice()
        if choice == 1:
            while newPerson != "done":
                newPerson = input("Input your name. (type 'done' when you're finished!\n")
                                
                if newPerson != "done": myArray.append(newPerson)
        elif choice == 2:
            for i in myArray:
                print(i)
        elif choice == 3:
            if len(myArray) != 0:
                index = int(input("Enter the index: 1-%s\n" % len(myArray)))
                print(myArray[index-1])
            else:
                print("No names")
        elif choice == 4:
            myArray = []
        else:
            exit()

def getUserChoice():
    choice = input("""
1. Enter New Name
2. Display All Names
3 – Display Specific name by index
4 – Clear list of names
5 – Exit
""")
    return int(choice)
    

if __name__ == "__main__":
    main()
