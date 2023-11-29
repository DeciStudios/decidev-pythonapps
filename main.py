import glob,os,subprocess,sys

def getFiles():
    global files
    files = []
    files = glob.glob(r".\files\*.py")
   

def chooseApp():
    print(len(files))
    for f in range(len(files)):
        print(f"{f+1}. {os.path.splitext(os.path.basename(files[f]))[0]}")
    choice = input("Enter a number")
    try:
        choice = int(choice)-1
        os.system(f"python {files[choice]}")
        chooseApp()
    except:
        print("Invalid input!")
        chooseApp()
    print(files[choice])
    
    

getFiles()
chooseApp()
