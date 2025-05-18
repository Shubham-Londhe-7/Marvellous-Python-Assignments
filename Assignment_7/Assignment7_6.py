
def chkPrime(value):
    count = 0
    for i in range(1,value+1):
        if ((value % i) == 0):
            count = count + 1
    if (count <= 2):
        return True
    else:
        return False

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enter elements :")
    for i in range(size):
        no = int(input())
        data.append(no)
    print("Entered list :",data)

    Fdata = list(filter(chkPrime,data))
    print("Prime numbers :",Fdata)
    
if __name__ == "__main__":
    main()