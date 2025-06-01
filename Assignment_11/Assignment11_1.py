i = 1

def Display(value):
    global i
    if(i<=value):
        print(i,end=" ")
        i += 1
        Display(value)

def main():
    print("Enter number :")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()