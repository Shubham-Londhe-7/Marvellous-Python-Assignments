import os

def main():
    print("Enter file name that you want to read :")
    fName = input()

    ret = os.path.exists(fName)

    if(ret == True):
        fobj = open(fName,"r")
        data = fobj.read()
        print("Content of file : \n",data)
        fobj.close()
    else:
        print("File not exixt")

if __name__ == "__main__":
    main()