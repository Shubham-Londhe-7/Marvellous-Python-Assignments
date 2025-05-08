# Add() which accepts to numbers and give addition of those numbers

def Add(value1, value2):
    result = value1 + value2
    return result

def main():
    print("Enetr first number : ")
    No1 = int(input())

    print("Enetr second number : ")
    No2 = int(input())

    ret = Add(No1,No2)

    print("Addition of two numbers is :",ret)


if __name__ == "__main__":
    main()