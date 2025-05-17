from functools import reduce

def chkPrime (A):
    count = 0
    for i in range (1,A+1):
        if (A % i) == 0:
            count = count + 1
    if count > 2:
        return False
    else:
        return True
    
Multiply = lambda A : A * 2

def Max(A,B):
    if A > B:
        return A
    else:
        return B

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enetr elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)
    
    print("Input data : ",data)

    Fdata = list(filter(chkPrime,data))
    print("Filter data : ",Fdata)

    Mdata = list(map(Multiply,Fdata))
    print("Map data : ",Mdata)

    Rdata = reduce(Max,Mdata)
    print("Reduce data : ",Rdata)

if __name__ == "__main__":
    main()