# function which accept name and display length 

def getLength(data):
    for i in range(len(data)):
        i = 1 + i
    return i

def main():
    print("Enter Name : ")
    name = input()

    ret = getLength(name)

    print("Length of name is : ",ret)

if __name__ == "__main__":
    main()