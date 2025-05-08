# ChkNum() which accepts one parameter to check even or odd number

def ChkNum(value):
    if ((value % 2) == 0):
        return True
    else:
        return False

def main():
    print("Enter a number : ")
    No = int(input())

    ret = ChkNum(No)

    if (ret == True):
        print("Number is even")
    else:
        print("Number is odd")

if __name__ == "__main__":
    main()