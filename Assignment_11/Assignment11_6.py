i = 1
sum = 0

def Sum_N(value):
    global i
    global sum

    if(i <= value):
        sum = sum + i
        i = i + 1
        Sum_N(value)
    return sum

def main():
    print("Enter number :")
    no = int(input())

    ret = Sum_N(no)
    print("Sum  of first",no,"natural numbers is :",ret)

if __name__ == "__main__":
    main()