import sys
import os

def CopyContent(newFile, existingFile):
    ret = os.path.exists(existingFile)
    if(ret == True):
        fobj = open(existingFile,"r")
        data = fobj.read()
        fobj.close()
    else:
        print(existingFile,"Not Exist")
    
    ret = os.path.exists(newFile)
    if(ret == True):
        print("This file name is invalid")
    else:
        nfobj = open(newFile,"w")
        nfobj.write(data)
        nfobj.close()
        print("Contents copied Successfully")

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to copy contents of existing file into new file")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  NewFileName  ExistingFileName")
        
        else:
            print("Use the given flags as :")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):
        CopyContent(sys.argv[1],sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
    

if __name__ == "__main__":
    main()