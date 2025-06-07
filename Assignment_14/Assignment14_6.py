
class Calculator:
    def __init__(self, value1, value2):
        self.No1 = value1
        self.No2 = value2

    def Addition(self):
        print("Addition is :",self.No1+self.No2)
    
    def Subtraction(self):
        print("Subtraction is :",self.No1-self.No2)
    
    def Multiply(self):
        print("Mulltiplication is :",self.No1*self.No2)
    
    def Divide(self):
        print("Divison is :",self.No1/self.No2)

def main():
    while(1):
        print("Enter First number : ")
        val1 = int(input())
        print("Enter Second number : ")
        val2 = int(input())

        print("Addition : 1 \n" \
        "Subtraction : 2 \n" \
        "Multiplication : 3 \n" \
        "Division : 4 \n" \
        "Exit : 5")

        print("Enter your choice : ")
        no = int(input())

        obj = Calculator(val1,val2)

        if(no == 1):
            obj.Addition()
        elif(no == 2):
            obj.Subtraction()
        elif(no == 3):
            obj.Multiply()
        elif(no == 4):
            obj.Divide()
        elif(no == 5):
            return
        else:
            print("Please enter correct choice")

if __name__ == "__main__":
    main()