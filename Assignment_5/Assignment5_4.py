
def chkLargest(value):
    if value[0] > value[1]:
        return value[0]
    elif value[1] > value[2]:
        return value[1]
    else:
        return value[2]

def main():
    print("Enter three numbers : ")
    data = list()
    for i in range(3):
        no = int(input())
        data.append(no)
    
    ret = chkLargest(data)

    print("Largest number is : ",ret)

if __name__ == "__main__":
    main()