
def chkLargest(value):
    max = 0
    for i in range(len(value)):
        if max > value[i]:
            max = max
        else:
            max = value[i]
    return max

def main():
    print("Enter 5 numbers : ")
    data = list()
    for i in range(5):
        no = int(input())
        data.append(no)
    
    ret = chkLargest(data)

    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()