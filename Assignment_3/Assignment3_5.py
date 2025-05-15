# return addition of prime numbers from list

import MarvellousNum

def ListPrime(value):
    sum = 0
    PrimeNum = list()
    for i in range (len(value)):
        if (MarvellousNum.ChkPrime(value[i]) == True):
            PrimeNum.append(value[i])
            sum = sum + value[i]
    print("Prime numbers are : ")
    print(PrimeNum)
    return sum

def main():
    print("Enter number of elemnts : ")
    size = int(input())

    data = list()
    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    print(data)

    ret = ListPrime(data)

    print("Addition of prime numbers from list is : ",ret)

if __name__ == "__main__":
    main()