# frequency of a number in list after adding it in list

def checkFreq(nums,key):
    count = 0
    for i in range(len(nums)):
        if(nums[i] == key):
            count = count + 1
    return count

def main():
    print("Enter number of elements : ")
    size = int(input())

    data = list()
    print("Enter elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    print("Enter element to search : ")
    value = int(input())

    ret = checkFreq(data,value)
    print("Frequency of that number from list is : ",ret)

if __name__ == "__main__":
    main()