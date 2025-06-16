import sys
import os
import hashlib

def CalculateCheckSum(path, BlockSize = 1024):
    fobj = open(path,"rb")

    hobj = hashlib.md5()

    buffer = fobj.read(BlockSize)
    while(len(buffer) > 0):
        hobj.update(buffer)
        buffer = fobj.read(BlockSize)

    fobj.close()

    return hobj.hexdigest()

def DirectoryDuplicate(DirectoryName):
    flag = os.path.isabs(DirectoryName)

    if(flag == False):
        DirectoryName = os.path.abspath(DirectoryName)

    flag = os.path.exists(DirectoryName)

    if(flag == False):
        print("The path is invalid")
        exit()

    flag = os.path.isdir(DirectoryName)

    if(flag == False):
        print("Path is valid but target is not directory")
        exit()
    
    Duplicate = {}

    for FolderName, SubFolderNames, FileNames in os.walk(DirectoryName):                                                                
        for fname in FileNames:
            fname = os.path.join(FolderName,fname)
            checkSum = CalculateCheckSum(fname)
            
            if checkSum in Duplicate:
                Duplicate[checkSum].append(fname)
            else:
                Duplicate[checkSum] = [fname] 
    
    return Duplicate

def DirectoryDuplicateRemoval(Path):
    MyDict = DirectoryDuplicate(Path)
    Result = list(filter(lambda X : len(X) > 1, MyDict.values()))

    FileName = "Log.txt"
    
    fobj = open(FileName,"w")


    Border = "-"*63

    fobj.write(Border+"\n")
    fobj.write("This is a log file of Marvellous Automation Script \n")
    fobj.write("This is a directory cleaner script used display duplicate files \n")
    fobj.write(Border+"\n")
    fobj.write("\n\n\n\n")

    Count = 0
    Cnt = 0

    for value in Result:
        for subValue in value:
            Count += 1
            if(Count > 1):
                fobj.write(subValue)
                fobj.write("\n")
                os.remove(subValue)
                Cnt += 1
        Count = 0
    fobj.write("Total deleted file : ")
    fobj.write(str(Cnt))
    fobj.write("\n\n\n\n")
    fobj.write(Border+"\n")
    fobj.write(Border+"\n")
    print("Total deleted file :",Cnt)

                
def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to delete duplicate files")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName")
        
        else:
            DirectoryDuplicateRemoval(sys.argv[1])

    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()