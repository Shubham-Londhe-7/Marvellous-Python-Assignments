
def chkPalindrome(value):
    end = len(value)-1
    for i in range(int(len(value)/2)):
        if value[i] != value[end]:
            return False
        end = end - 1
    return True

def main():
    print("Enter a string :")
    data = input()

    ret = chkPalindrome(data)

    if ret == True:
        print(data,"is Palindrome")
    else:
        print(data,"is NOT Palindrome")

if __name__ == "__main__":
    main()
