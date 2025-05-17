from functools import reduce

chkEven = lambda A : A % 2 == 0
Suqare = lambda A : A**2
Sum = lambda A,B : A + B

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enetr elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Input data : ",data)

    Fdata = list(filter(chkEven,data))
    print("Filter data : ",Fdata)

    Mdata = list(map(Suqare,Fdata))
    print("Map data : ",Mdata)

    Rdata = reduce(Sum,Mdata)
    print("Reduce data : ",Rdata)

if __name__ == "__main__":
    main()