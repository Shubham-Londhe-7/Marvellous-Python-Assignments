
def addDigit(value):
    ans = 0
    for i in range(len(value)):
        ans = ans + int(value[i])
    return ans

def main():
    print("Enter Number : ")
    no = input()

    ret = addDigit(no)
    print("Addition of digits is : ",ret)

if __name__ == "__main__":
    main()