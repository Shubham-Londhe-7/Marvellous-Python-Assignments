# check number is positive , nagative or else

def checkNum(value):
    if (value > 0):
        print("Number is Positive")
    elif (value < 0):
        print("Number is Negative")
    else:
        print("Number is Zero")

def main():
    print("Enter number : ")
    No = int(input())

    checkNum(No)

if __name__ == "__main__":
    main()