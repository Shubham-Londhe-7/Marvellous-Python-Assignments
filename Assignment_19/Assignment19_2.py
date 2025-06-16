import sys
import os

def DirectoryRename(DirectoryName, ExistingExtension, NewExtension):
    if(os.path.exists(DirectoryName)):
        for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
            print("Scanning folder  is : ",FolderName)
            for fName in FileNames:
                if(str(fName).endswith(ExistingExtension)):
                    old_fileName = os.path.join(FolderName, fName)
                    fileWithoutExten = os.path.splitext(fName)[0]
                    new_fileName = fileWithoutExten + NewExtension
                    new_fileName = os.path.join(FolderName, new_fileName)
                    os.rename(old_fileName, new_fileName)
                    
    else:
        print("Invalid directory name")

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to change the extension of existing files with new extension")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName  ExistingExtension  NewExtension")
        
        else:
            print("Use the given flags as :")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 4):
        DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()