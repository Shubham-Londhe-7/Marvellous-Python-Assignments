
def chkPrime(value):
    count = 0
    for i in range (1,value+1):
        if ((value % i ) == 0):
            count = count + 1
    if count <= 2:
        return True
    else:
        return False

def main():
    print("Enter number : ")
    no = int(input())

    ret = chkPrime(no)

    if ret == True:
        print(no,"is a prime number")
    else:
        print(no,"is not a prime number")

if __name__ == "__main__":
    main()