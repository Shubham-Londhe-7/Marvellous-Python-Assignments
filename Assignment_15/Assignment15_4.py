import sys
import os

def CompareContent(File1, File2):
    ret = os.path.exists(File1)
    if(ret == True):
        fobj1 = open(File1,"r")
        contentOfFile1 = fobj1.read()
        fobj1.close()
    else:
        print(File1,"Not Exist")
    
    ret = os.path.exists(File2)
    if(ret == True):
        fobj2 = open(File2,"r")
        contentOfFile2 = fobj2.read()
        fobj2.close()
    else:
        print(File2,"Not Exist")

    if(contentOfFile1 == contentOfFile2):
        return True
    else:
        return False

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to compare contents of two files")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  FileName1  FileName2")
        
        else:
            print("Use the given flags as :")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):
        ret = CompareContent(sys.argv[1],sys.argv[2])

        if(ret == True):
            print("Success")
        else:
            print("Failure")
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")
    

if __name__ == "__main__":
    main()