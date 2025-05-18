
square = lambda A : A**2
cube = lambda A : A**3

def main():
    print("Enter number : ")
    no = int(input())

    ret = square(no)
    print("Square :",ret)

    ret = cube(no)
    print("cube :",ret)
    
if __name__ == "__main__":
    main()