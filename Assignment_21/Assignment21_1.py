import psutil
import sys
import os

def ProcInfo():
    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name','pid','username'])
        print(info)

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to display information of running processes")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py")

    elif(len(sys.argv) == 1):
        ProcInfo()

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()