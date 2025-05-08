# number is divisible by 5

def checkNum(value):
    if ((value % 5) == 0):
        return True
    else:
        return False

def main():
    print("Enetr Number : ")
    No = int(input())

    ret = checkNum(No)

    if (ret == True):
        print("Number IS divisible by 5 ")
    else:
        print("Number IS NOT divisible by 5")

if __name__ == "__main__":
    main()