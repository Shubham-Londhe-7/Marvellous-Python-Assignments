# addition of elements of list

def addData(value):
    ans = 0
    for num in value:
        ans = ans + num
    return ans

def main():
    print("Enter size : ")
    size = int(input())

    data = list()

    print("Enter Numbers : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)

    ret = addData(data)

    print("Addition of all numbers is : ",ret)
        

if __name__ == "__main__":
    main()