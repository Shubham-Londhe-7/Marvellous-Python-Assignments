# lambda fn for multiplication
def main():
    mult = lambda A,B : A * B

    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    ret = mult(no1,no2)
    print("Multiplication is : ",ret)

if __name__ == "__main__":
    main()