fact = 1

def Factorial(value):
    global fact
    if(value >= 1):
        fact = fact * value
        value -= 1
        Factorial(value)
    return fact

def main():
    print("Enter number :")
    no = int(input())

    ret = Factorial(no)
    print("Factorial is :",ret)

if __name__ == "__main__":
    main()