
class Numbers:
    def __init__(self, No):
        self.Value = No

    def ChkPrime(self):
        count = 0
        for i in range(1,self.Value+1):
            if(self.Value % i == 0):
                count += 1
        if(count <= 2):
            return True
        else:
            return False

    def ChkPerfect(self):
        perfect = self.SumFactors() - self.Value
    
        if(perfect == self.Value):
            return True
        else:
            return False

    def Factors(self):
        for i in range(1,self.Value+1):
            if(self.Value%i == 0):
                print(i,end=" ")
        print()

    def SumFactors(self):
        factors = 0
        for i in range(1,self.Value+1):
            if(self.Value%i == 0):
                factors += i
        return factors

def main():
    print("Enter number :")
    no = int(input())

    obj = Numbers(no)
    
    ret = obj.ChkPrime()
    if(ret):
        print("Number is Prime")
    else:
        print("Number is not prime")

    ret = obj.ChkPerfect()
    if(ret):
        print("Number is Perfect")
    else:
        print("Number is not Perfect")

    print("Factors are : ")
    obj.Factors()
    
    ret = obj.SumFactors()
    print("Addition of Factors is :",ret)


if __name__ == "__main__":
    main()