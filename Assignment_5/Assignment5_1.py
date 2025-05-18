
def Sum(value1,value2):
    return value1 + value2

def Difference(value1,value2):
    return value1 - value2

def Product(value1,value2):
    return value1 * value2

def Division(value1,value2):
    return value1 / value2

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    sret = Sum(no1,no2)
    print("Sum : ",sret)

    dret = Difference(no1,no2)
    print("Difference : ",dret)

    dret = Product(no1,no2)
    print("Product : ",dret)

    dret = Division(no1,no2)
    print("Division : ",dret)

if __name__ == "__main__":
    main()