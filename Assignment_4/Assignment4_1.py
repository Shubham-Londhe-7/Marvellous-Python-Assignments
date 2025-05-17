# lambda function power of two 

def main():
    Power = lambda A : A**2

    print("Enter number : ")
    no = int(input())

    ret = Power(no)
    print("Power is : ",ret)

if __name__ == "__main__":
    main()