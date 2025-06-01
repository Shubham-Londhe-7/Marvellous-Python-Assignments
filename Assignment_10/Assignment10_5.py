from functools import reduce

def ChkPrime(no):
    i = 2
    while(i <= int(no/2)):
        if(no % i == 0):
            return False
        i = i + 1
    return True

def Max(no1, no2):
    largest = no1
    if(largest < no2):
        largest = no2

    return largest


def main():
    print("Enter total no of elements in the list: ")
    size = int(input())

    inputData = []

    print("Enter", size, " elements : ")
    for i in range(size):
        value = int(input())
        inputData.append(value)
    
    print(inputData)
    
    FData = list(filter(ChkPrime, inputData))
    print("List after filter : ", FData)

    MData = list(map(lambda no : (no*2), FData))
    print("List after map : ", MData)

    RData = reduce(Max, MData)
    print("Output of reduce : ", RData)



if __name__ == "__main__":
    main()