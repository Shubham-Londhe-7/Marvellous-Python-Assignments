import psutil
import sys
import os
import time

def MakeDirectoryLog(DirectoryName):

    timestamp = time.ctime()
    FileName = "Process%s"%timestamp
    FileName = FileName.replace(":","")
    FileName = FileName.replace(" ","_")
    FileName = os.path.join(DirectoryName,FileName)

    fobj = open(FileName,"w")
    fobj.write('This file is created at ')
    fobj.write(timestamp+"\n")
    fobj.write("\n")
    fobj.close()

    ProcInfoLog(FileName)

def ProcInfoLog(File):
    Border = "-"*80
    fobj = open(File,'a')
    fobj.write(Border+"\n")
    fobj.write("\t\t Current running processes \t\t")
    fobj.write("\n")
    fobj.write(Border+"\n")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=['name','pid','username'])
        fobj.write(str(info))
        fobj.write("\n\n")
    
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")

    fobj.close()


def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to store information of running process in given directory as logfile")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName")
        
        else:
            os.mkdir(sys.argv[1])
            MakeDirectoryLog(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()