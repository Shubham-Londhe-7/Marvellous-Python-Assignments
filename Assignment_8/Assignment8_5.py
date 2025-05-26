
import threading

def display1():
    for i in range(1,51):
        print(i,end=" ")
    print()

def display2():
    for i in range(50,0,-1):
        print(i,end=" ")
    print()

def main():
    Thread1 = threading.Thread(target = display1)
    Thread1.start()
    Thread1.join()

    print("Executuion of Thread1 completed")

    Thread2 = threading.Thread(target = display2)
    Thread2.start()
    Thread2.join()   

    print("Executuion of Thread2 completed") 

if __name__ == "__main__":
    main()