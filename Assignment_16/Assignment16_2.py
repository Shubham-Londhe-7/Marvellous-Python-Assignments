
def main():
    fobj = open("data.txt","r")
    data = fobj.read()
    print("Contents od data.txt file are :\n",data)
    fobj.close()

if __name__ == "__main__":
    main()