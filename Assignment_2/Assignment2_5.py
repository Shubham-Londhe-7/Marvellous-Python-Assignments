
def checkPrime(value):
    count = 0
    for i in range(1,value+1):
        if value%i == 0:
            count = count + 1
    if(count > 2):
        return False
    else:
        return True

def main():
    print("Enter Number : ")
    no = int(input())

    ret = checkPrime(no)

    if ret == True:
        print("It is prime number")
    else:
        print("It is NOT a prime number")

if __name__ == "__main__":
    main()