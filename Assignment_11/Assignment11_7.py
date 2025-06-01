
i = 0

def Display(no):
    global i

    if(i < no):
        j = 0
        while(j < no and j <= i):
            print("*",end=" ")
            j = j + 1
        print()
        i = i + 1
        Display(no)

def main():
    print("Enter number :")
    value = int(input())

    Display(value)

if __name__ == "__main__":
    main()