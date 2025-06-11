import os

def countFrequency(FileName, data):
    if(os.path.exists(FileName)):
        fobj = open(FileName,"r")
        FileData = fobj.read()
        Words = FileData.split()
        return Words.count(data)
    else:
        print(FileName,"not exists") 

def main():
    print("Enter file name :")
    fName = input()

    print("Enter the string for counting frequency :")
    word = input()

    ret = countFrequency(fName, word)

    print("Frequency of ",word,"in ",fName,"file is :",ret)

if __name__ == "__main__":
    main()