
def chkAge(value):
    if value >= 18:
        return True
    else:
        return False

def main():
    print("Enter age : ")
    age = int(input())

    ret = chkAge(age)

    if ret == True:
        print("Eligible for voting")
    else:
        print("NOT eligible for voting")

if __name__ == "__main__":
    main()