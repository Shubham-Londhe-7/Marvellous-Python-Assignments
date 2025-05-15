'''
* * * * *
* * * *
* * *
* *
*
'''
def Display(value):
    for i in range(value):
        for j in range(value):
            if (i <= j):
                print("*",end=" ")
        print()

def main():
    print("Enter Number : ")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()