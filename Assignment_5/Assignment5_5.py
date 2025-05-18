
def chkEven(value):
    if (value % 2) == 0:
        return True
    else:
        return False

def main():
    print("Enter number : ")
    no = int(input())

    ret = chkEven(no)

    if ret == True:
        print(no," is an Even number")
    else:
        print(no," is an Odd number")

if __name__ == "__main__":
    main()