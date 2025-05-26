
import multiprocessing

def Square(values):
    for elements in values:
        print(elements**2,end=" ")
    print()

def main():
    print("Enter number of elements :")
    size = int(input())

    data = list()
    print("Enter numbers :")
    for i in range(size):
        no1 = int(input())
        data.append(no1)
    print(data)

    T1 = multiprocessing.Process(target = Square, args = (data,))
    T1.start()
    T1.join()

if __name__ == "__main__":
    main()