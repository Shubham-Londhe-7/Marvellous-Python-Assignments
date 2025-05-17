from functools import reduce

filterfn = lambda A : ((A >= 70) and (A <= 90))
Increase = lambda A : A + 10
Product = lambda A,B : A * B

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enetr elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Input data : ",data)

    Fdata = list(filter(filterfn,data))
    print("Filter data : ",Fdata)

    Mdata = list(map(Increase,Fdata))
    print("Map data : ",Mdata)

    Rdata = reduce(Product,Mdata)
    print("Reduce data : ",Rdata)

if __name__ == "__main__":
    main()