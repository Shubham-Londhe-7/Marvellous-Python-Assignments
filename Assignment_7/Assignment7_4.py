from functools import reduce

product = lambda A,B : A * B

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Entered list :",data)

    Fdata = reduce(product,data)
    print("Product :",Fdata)
    
if __name__ == "__main__":
    main()