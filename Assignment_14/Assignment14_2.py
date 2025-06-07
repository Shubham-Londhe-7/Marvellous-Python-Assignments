
class Rectangle:
    def __init__(self,len,wid):
        self.length = len
        self.width = wid
    
    def calculatePerimeter(self):
        Perimeter = 2*(self.length + self.width)
        return Perimeter

    def calculateArea(self):
        Area = self.length * self.width
        return Area

def main():
    print("Enter length : ")
    no1 = int(input())

    print("Enter breadth : ")
    no2 = int(input())

    obj1 = Rectangle(no1,no2)

    ret = obj1.calculateArea()
    print("Area is :",ret)

    ret = obj1.calculatePerimeter()
    print("Perimeter is :",ret)

if __name__ == "__main__":
    main()