'''
*****
*****
*****
*****
*****

'''
def Display(value):
    for i in range (value):
        for j in range(value):
            print("*", end = " ")
        print()
        

def main():
    print("Enter number : ")
    no = int(input())

    Display(no)

if __name__ == "__main__":
    main()