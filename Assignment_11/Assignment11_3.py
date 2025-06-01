i = 0
sum = 0

def sumOfDigits(value):
    global i
    global sum
    
    if(i < len(value)):
        sum = sum + int(value[i])
        i = i + 1
        sumOfDigits(value)
    return sum

def main():
    print("Enter number :")
    no = input()

    ret = sumOfDigits(no)
    print("Sum of digits is :",ret)

if __name__ == "__main__":
    main()