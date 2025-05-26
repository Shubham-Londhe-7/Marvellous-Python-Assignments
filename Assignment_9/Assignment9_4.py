import threading
import multiprocessing
import time

def Display():
    for i in range(1,10000000):
        print(i,end=" ")
    print()

def main():
    start_time = time.time()
    Display()
    end_time = time.time()
    Function_time = end_time - start_time

    start_time = time.time()
    T1 = threading.Thread(target = Display)
    T1.start()
    T1.join()
    end_time = time.time()
    Threading_time = end_time - start_time

    start_time = time.time()
    P1 = multiprocessing.Process(target = Display)
    P1.start()
    P1.join()
    end_time = time.time()
    Multiprocessing_time = end_time - start_time

    print("Time required for normal function :",Function_time)
    print("Time required for Threading :",Threading_time)
    print("Time required for Multiprocessing :",Multiprocessing_time)
    

if __name__ == "__main__":
    main()