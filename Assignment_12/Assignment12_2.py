
class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self,value1):
        self.Radius = value1

    def CalculateArea(self):
        area = Circle.PI * self.Radius**2
        self.Area = area
        
    def CalculateCircumference(self):
        circum = 2 * Circle.PI * self.Radius
        self.Circumference = circum

    def Display(self):
        print("Radius is :",self.Radius)
        print("Area is :",self.Area)
        print("Circumference is :",self.Circumference)

def main():
    obj1 = Circle()
    obj1.Accept(10)
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()
    print("------------------------")
    obj2 = Circle()
    obj2.Accept(98.56)
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()
    print("------------------------")
    obj3 = Circle()
    obj3.Accept(111.546)
    obj3.CalculateArea()
    obj3.CalculateCircumference()
    obj3.Display()

if __name__ == "__main__":
    main()