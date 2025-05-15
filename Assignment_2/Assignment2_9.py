
def countDigit(value):
    for i in range(len(value)):
        count = 1 + i
    return count

def main():
    print("Enter Number : ")
    no = input()

    ret = countDigit(no)
    print("Number of digits are : ",ret)

if __name__ == "__main__":
    main()