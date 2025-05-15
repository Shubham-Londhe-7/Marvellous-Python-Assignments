# return factors of a number 

def factors(value):
    result = []

    for i in range(1,value):
        if value%i == 0:
            result.append(i)
    print(result)
    ans = 0
    for i in range (len(result)):
        ans = ans + result[i]
    return ans

def main():
    print("Enter Number : ")
    no = int(input())

    ret = factors(no)
    print("Addition of factors is : ",ret)

if __name__ == "__main__":
    main()