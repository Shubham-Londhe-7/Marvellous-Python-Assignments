
import multiprocessing

def Factorial(value):
    fact = 1
    for i in range(1,value+1):
        fact = fact * i
    return fact

def main():
    print("Enter number of elements :")
    size = int(input())

    data = list()
    print("Enter numbers :")
    for i in range(size):
        no1 = int(input())
        data.append(no1)
    print(data)
    
    P = multiprocessing.Pool()
    ret = list(map(Factorial,data))

    P.close()
    P.join()

    print("Factorial of numbers in list :",ret)

if __name__ == "__main__":
    main()