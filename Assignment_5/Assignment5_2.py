
def isVowel(value):
    if (value == "a" or value == "e" or value == "i" or value == "o" or value == "u"):
        return True
    else:
        return False

def main():
    print("Enter Character : ")
    Ch = input()

    ret = isVowel(Ch)

    if ret == True:
        print(Ch," is a Vowel")
    else:
        print(Ch," is a Cosonant")
    

if __name__ == "__main__":
    main()