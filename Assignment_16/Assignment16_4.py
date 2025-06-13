
def Write(numbers):
    fobj = open("numbers.txt","w")
    for i in range(10):
        fobj.write(numbers[i])
        fobj.write("\n")
    fobj.close()

def main():
    data = list()
    print("Enter 10 numbers to enter into file :")
    for i in range(10):
        no = input()
        data.append(no)
    
    Write(data)

if __name__ == "__main__":
    main()