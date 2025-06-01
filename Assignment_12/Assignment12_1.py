
class Demo:
    value = None        # class variable

    def __init__(self,A ,B):        # parameterized const
        self.no1 = A        # instance variable
        self.no2 = B        # instance variable

    def Fun(self):          # instance method
        print(self.no1)
        print(self.no2)
    
    def Gun(self):          # instance method
        print(self.no1)
        print(self.no2)

def main():
    Obj1 = Demo(11,21)          # object creation of class
    Obj2 = Demo(51,101)

    Obj1.Fun()
    Obj1.Gun()
    Obj2.Fun()
    Obj2.Gun()

if __name__ == "__main__":
    main()