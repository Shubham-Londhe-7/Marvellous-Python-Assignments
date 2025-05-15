
import Arithmatic

def main():
    print("Enter first number : ")
    no1 = int(input())

    print("Enter second number : ")
    no2 = int(input())

    print("Enter your Choice : ")
    print("For Addition : 1")
    print("For Substraction : 2")
    print("For Multiplication : 3")
    print("For Division : 4")
    
    choice = int(input())

    if choice == 1:
        ret = Arithmatic.Add(no1,no2)
        print("Addition is : ",ret)
    elif choice == 2:
        ret = Arithmatic.Sub(no1,no2)
        print("Substraction is : ",ret)
    elif choice == 3:
        ret = Arithmatic.Mult(no1,no2)
        print("Multiplication is : ",ret)
    elif choice == 4:
        ret = Arithmatic.Div(no1,no2)
        print("Division is : ",ret)
    else:
        print("Enter correct Choice")


if __name__ == "__main__":
    main()