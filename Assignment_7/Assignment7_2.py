
double = lambda A : A * 2

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Entered list :",data)

    Mdata = list(map(double,data))
    print("Doubled lis :",Mdata)
    
if __name__ == "__main__":
    main()