import os
def getCar(i,reverse):
    o = getSpaces(i) + "    ____\n"
    o += getSpaces(i) + " __/  |_\_\n"
    o += getSpaces(i) + reverse+"  _     _``-.\n"
    o += getSpaces(i) + "'-(_)---(_)--'\n"
    return o

def getSpaces(i):
    return " " * i
while True:
    for i in range(20):
        print(getCar(i*5,"|"))
        os.system('cls')
    for i in range(20,0,-1):
        print(getCar(i*5,"*"))
        os.system('cls')

