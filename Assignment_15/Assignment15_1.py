
import os

def fileExists(Filename):
    if(os.path.exists(Filename)):
        return True
    else:
        return False

def main():
    print("Enter file name that you want to check :")
    fName = input()

    ret = fileExists(fName)

    if(ret == True):
        print(fName,"exists")
    else:
        print(fName,"Not exist")

if __name__ == "__main__":
    main()