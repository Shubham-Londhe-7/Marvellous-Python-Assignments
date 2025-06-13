
import os

def CopyContents(Source, Destination):
    if(os.path.exists(Source)):
        sobj = open(Source,"r")
        data = sobj.read()
        sobj.close()
    else:
        print("Source file not exist")
    
    if(os.path.exists(Destination)):
        dobj = open(Destination,"w")
        dobj.write(data)
        print("Data copied Successfully")
        dobj.close()
    else:
        print("Destination file not exist")

def main():
    print("Enter name of source file :")
    File1 = input()

    print("Enter name of destination file :")
    File2 = input()

    CopyContents(File1, File2)

if __name__ == "__main__":
    main()