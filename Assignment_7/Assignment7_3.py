
chkEven = lambda A : (A % 2) == 0

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Entered list :",data)

    Fdata = list(filter(chkEven,data))
    print("Even numbers :",Fdata)
    
if __name__ == "__main__":
    main()