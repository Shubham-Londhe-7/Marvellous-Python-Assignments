from functools import reduce

numbers = lambda A : 70 <= A <= 90
Increase = lambda A : A+10
Product = lambda A, B : A * B

def main():
    print("Enter number of elements :")
    size = int(input())

    data = list()
    print("Enter numbers :")
    for i in range(size):
        no1 = int(input())
        data.append(no1)
    print("Input list :",data)

    Fdata = list(filter(numbers,data))
    print("List after filter :",Fdata)
   
    Mdata = list(map(Increase,Fdata))
    print("List after map :",Mdata)

    Rdata = reduce(Product,Mdata)
    print("Output of reduce :",Rdata)

if __name__ == "__main__":
    main()