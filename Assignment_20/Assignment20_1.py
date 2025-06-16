import sys
import os
import hashlib

def DirectoryCheckSum(DirectoryName, BlockSize = 1024):
    if(os.path.exists(DirectoryName)):
        for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
            print("Scanning folder is :",FolderName)
            print("\n\n")
            print("FileName \t\t\t CheckSum")
            for fName in FileNames:
                File = os.path.join(FolderName,fName)
                fobj = open(File,"rb")
                hobj = hashlib.md5()
                buffer = fobj.read(BlockSize)
                while(len(buffer) > 0):
                    hobj.update(buffer)
                    buffer = fobj.read(BlockSize)
                fobj.close()
                checkSum = hobj.hexdigest()
                print(fName,"\t\t\t",checkSum)
    else:
        print("Invalid directory name")
                


def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to display checksum of files in directory")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName")
        
        else:
            DirectoryCheckSum(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()