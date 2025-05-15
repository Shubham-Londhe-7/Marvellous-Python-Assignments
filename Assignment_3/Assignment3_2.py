# max from list

def checkMAX(value):
    max = value[0]
    for num in value:
        if (num > max):
            max = num
        else:
            num = max
    return max
        

def main():
    print("Enter size : ")
    size = int(input())

    data = list()

    print("Enter Numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    ret = checkMAX(data)

    print("Maximum number from list is : ",ret)

if __name__ == "__main__":
    main()