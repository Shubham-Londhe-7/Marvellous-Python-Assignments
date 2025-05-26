import threading

def addEvenFactors(value):
    sum = 0
    for i in range(1, value+1):
        if((value % i) == 0):
            if((i % 2) == 0):
                sum = sum + i
    print("Addition of even factors is :",sum)

def addOddFactors(value):
    sum = 0
    for i in range(1, value+1):
        if((value % i) == 0):
            if((i % 2) != 0):
                sum = sum + i
    print("Addition of odd factors is :",sum)

def main():
    print("Enter number : ")
    no = int(input())

    evenfactor = threading.Thread(target = addEvenFactors, args = (no,))
    evenfactor.start()
    evenfactor.join()

    oddfactor = threading.Thread(target = addOddFactors,args = (no,))
    oddfactor.start()
    oddfactor.join()

    print("Exit from main")

if __name__ == "__main__":
    main()