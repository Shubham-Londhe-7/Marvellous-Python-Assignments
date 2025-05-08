# accept number and " * " that number of times

def display(value):
    for i in range(value):
        print("*", end = " ")

def main():
    print("Enter Number : ")
    No = int(input())

    display(No)

if __name__ == "__main__":
    main()