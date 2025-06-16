import sys
import os


def DirectoryFileSearch(DirectoryName, Extension):
    if(os.path.exists(DirectoryName)):
        for FolderName, SubFolders, FileNames in os.walk(DirectoryName):
            for fname in FileNames:
                if(str(fname).endswith(Extension)):
                    print(fname)
    else:
        print("Invalid directory name")


def main():
    if(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This automation script is used to show files with given extension from given directory")
        
        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as")
            print("python ScriptName.py  DirectoryName  FileExtension")
        
        else:
            print("Use the given flags as :")
            print("--h : Used to display the help")
            print("--u : Used to display the usage")

    elif(len(sys.argv) == 3):
        DirectoryFileSearch(sys.argv[1],sys.argv[2])
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as :")
        print("--h : Used to display the help")
        print("--u : Used to display the usage")

if __name__ == "__main__":
    main()