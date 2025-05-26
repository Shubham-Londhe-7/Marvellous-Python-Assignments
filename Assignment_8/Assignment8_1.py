import threading

def DisplayEven():
    print("First 10 even numbers")
    for i in range (1,21):
        if(i % 2 == 0):
            print(i,end=" ")
    print()

def DisplayOdd():
    print("First 10 odd numbers")
    for i in range (1,21):
        if(i % 2 != 0):
            print(i,end = " ")

def main():
    even = threading.Thread(target = DisplayEven)
    even.start()
    
    odd = threading.Thread(target = DisplayOdd)
    odd.start()


if __name__ == "__main__":
    main()