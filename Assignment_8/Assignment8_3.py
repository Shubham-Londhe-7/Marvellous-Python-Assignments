import threading

def addEven(value):
    sum = 0
    for i in range(len(value)):
        if((value[i] % 2) == 0):
            sum = sum + value[i]
    print("Addition of Even elements is :",sum)

def addOdd(value):
    sum = 0
    for i in range(len(value)):
        if((value[i] % 2) != 0):
            sum = sum + value[i]
    print("Addition of Odd elements is :",sum)

def main():
    print("Enter number of elements :")
    size = int(input())

    data = list()
    print("Enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)

    evenlist = threading.Thread(target = addEven, args = (data,))
    evenlist.start()
    evenlist.join()

    oddlist = threading.Thread(target = addOdd, args = (data,))
    oddlist.start()
    oddlist.join()
    
if __name__ == "__main__":
    main()