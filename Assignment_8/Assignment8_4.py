
import threading

def numberOfSmall(value):
    count = 0
    for element in value:
        if("a" <= element <= "z"):
            count = count + 1
    print("Number of small characters is :",count)

def numberOfCapital(value):
    count = 0
    for element in value:
        if("A" <= element <= "9"):
            count = count + 1
    print("Number of capital characters is :",count)

def numberOfDigits(value):
    count = 0
    for element in value:
        if("0" <= element <= "9"):
            count = count + 1
    print("Number of digits are :",count)

def main():
    print("Enter data :")
    data = input()

    small = threading.Thread(target = numberOfSmall, args = (data,))
    small.start()

    capital = threading.Thread(target = numberOfCapital, args = (data,))
    capital.start()

    digits = threading.Thread(target = numberOfDigits, args = (data,))
    digits.start()

if __name__ == "__main__":
    main()