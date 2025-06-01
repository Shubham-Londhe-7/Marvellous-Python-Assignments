i = 0
count = 0

def countZero(value):
    global i
    global count

    if(i < len(value)):
        if(value[i] == "0"):
            count = count + 1
        i = i + 1
        countZero(value)
    return count

def main():
    print("Enter number :")
    no = input()
    ret = countZero(no)
    print("Number of zero's are :",ret)

if __name__ == "__main__":
    main()