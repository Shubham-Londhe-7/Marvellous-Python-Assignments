import sys
import os

def count(FileName):
    if(os.path.exists(FileName)):
        fobj = open(FileName,"r")
        data = fobj.read()

        Count = 0
        for i in range(len(data)):
            if(data[i] == "\n"):
                Count += 1
        print("Lines in given file are :",Count)

        for i in range(len(data)):
            if(data[i] == " "):
                Count += 1
        print("Words in given file are :",Count)

        for i in range(len(data)):
            if(data[i] == " " or data[i] == "\n"):
                Count += 0
            else:
                Count += 1
        print("Words in given file are :",Count)

        fobj.close()
        

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This script is used to count number of line, words, and characters in a given file")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  FileName")
        
        else:
            count(sys.argv[1])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
    

if __name__ == "__main__":
    main()