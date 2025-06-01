
class Arithmetic:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self,no1,no2):
        self.value1 = no1
        self.value2 = no2

    def Addition(self):
        result = self.value1 + self.value2
        return result
    
    def Subtraction(self):
        result = self.value1 - self.value2
        return result

    def Multiplication(self):
        result = self.value1 * self.value2
        return result

    def Division(self):
        result = self.value1 / self.value2
        return result

def main():
    obj1 = Arithmetic()
    obj1.Accept(10,11)
    ret = obj1.Addition()
    print("Addition is :",ret)
    ret = obj1.Subtraction()
    print("Subtraction is :",ret)
    ret = obj1.Multiplication()
    print("Multiplication is :",ret)
    ret = obj1.Division()
    print("Division is :",ret)
    print("----------------------------------------")
    obj2 = Arithmetic()
    obj2.Accept(90,15)
    ret = obj2.Addition()
    print("Addition is :",ret)
    ret = obj2.Subtraction()
    print("Subtraction is :",ret)
    ret = obj2.Multiplication()
    print("Multiplication is :",ret)
    ret = obj2.Division()
    print("Division is :",ret)
    print("----------------------------------------")
    obj3 = Arithmetic()
    obj3.Accept(1524,12)
    ret = obj3.Addition()
    print("Addition is :",ret)
    ret = obj3.Subtraction()
    print("Subtraction is :",ret)
    ret = obj3.Multiplication()
    print("Multiplication is :",ret)
    ret = obj3.Division()
    print("Division is :",ret)
    print("----------------------------------------")

if __name__ == "__main__":
    main()