result = 1
i = 0

def power(value,pow):
    global result
    global i

    if(i < pow):
        result = result * value
        i = i + 1
        power(value,pow)
    return result

def main():
    print("Enter number :")
    no = int(input())

    print("Enter power of number :")
    index = int(input())

    ret = power(no,index)
    print(index,"rd power of ",no,"is :",ret)

if __name__ == "__main__":
    main()