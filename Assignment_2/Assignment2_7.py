'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
'''
def Display(value):
    for i in range(1,value+1):
        for j in range(1,value+1):
            print(j, end = " ")
        print()

def main():
    print("Enter Number : ")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()