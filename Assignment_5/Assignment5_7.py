
def calArea(len, wid):
    area = len * wid
    return area

def calPerimeter(len, wid):
    perimeter = 2*(len + wid)
    return perimeter

def main():
    print("Enter length : ")
    length = float(input())

    print("Enter width : ")
    width = float(input())

    aret = calArea(length,width)
    print("Area : ",aret)

    pret = calPerimeter(length,width)
    print("Perimeter : ",pret)

if __name__ == "__main__":
    main()