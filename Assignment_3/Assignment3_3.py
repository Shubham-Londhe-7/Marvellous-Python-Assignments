# min from list

def checkMIN(value):
    min = value[0]
    for num in value:
        if (num < min):
            min = num
        else:
            num = min
    return min
        

def main():
    print("Enter size : ")
    size = int(input())

    data = list()

    print("Enter Numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    ret = checkMIN(data)

    print("Minimum number from list is : ",ret)

if __name__ == "__main__":
    main()