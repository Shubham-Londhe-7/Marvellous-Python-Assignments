import threading
import time

def Display():
    for i in range(1,6):
        print(i,end=" ")
    print()

def main():
    time.sleep(1)
    
    Thread1 = threading.Thread(target = Display())
    Thread1.start()
    Thread1.join()
    time.sleep(1)

    Thread2 = threading.Thread(target = Display())
    Thread2.start()
    Thread2.join()
    time.sleep(1)

    Thread3 = threading.Thread(target = Display())
    Thread3.start()
    Thread3.join()
    time.sleep(1)

if __name__ == "__main__":
    main()