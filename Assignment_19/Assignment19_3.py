import sys
import os
import shutil

def DirectoryCopy(ExistingDirectory, NewDirectory):
    if(os.path.exists(ExistingDirectory)):
        if not (os.path.exists(NewDirectory)):
            os.mkdir(NewDirectory)
            print("New directory created successfully as :",NewDirectory)
            for FolderName, SubFolders, FileNames in os.walk(ExistingDirectory):
                print("Existing Directory is :",FolderName)
                for fName in FileNames:
                    SourcePath = os.path.join(FolderName, fName)
                    DestPath = os.path.join(NewDirectory, fName)
                    shutil.copyfile(SourcePath, DestPath)
        else:
            print("Directory already exist")
    else:
        print("Invalid ExistingDirectory name")
        

def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to copy contents of existing directory into new directory")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  ExistingDirectoryName  NewDirectoryName")
        
        else:
            print("Use the given flags as :")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):
        DirectoryCopy(sys.argv[1],sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()