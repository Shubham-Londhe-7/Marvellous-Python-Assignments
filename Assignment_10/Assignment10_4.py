from functools import reduce

even = lambda A : (A % 2) == 0
square = lambda A : A**2
addition = lambda A, B : A + B

def main():
    print("Enter number of elements :")
    size = int(input())

    data = list()
    print("Enter numbers :")
    for i in range(size):
        no1 = int(input())
        data.append(no1)
    print("Input list :",data)

    Fdata = list(filter(even,data))
    print("List after filter :",Fdata)
   
    Mdata = list(map(square,Fdata))
    print("List after map :",Mdata)

    Rdata = reduce(addition,Mdata)
    print("Output of reduce :",Rdata)

if __name__ == "__main__":
    main()