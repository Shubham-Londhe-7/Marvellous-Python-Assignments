
class BankAccount:
    def __init__(self, acc_no,acc_holder):
        self.Account_number = acc_no
        self.name = acc_holder
        self.balance = 0
    
    def Deposit(self,amount):
        self.balance += amount
        print(amount,"Deposited Successfully !!")

    def Withdraw(self,amount):
        if(amount > self.balance):
            print("Insufficient Balance")
            return
        self.balance -= amount
        print(amount,"Withrawl Successfully !! ")
    
    def displayBalance(self):
        print("Available Balance :",self.balance)


def main():
    obj1 = BankAccount(110,"Shubam")
    obj1.Deposit(10000)
    obj1.displayBalance()

    obj1.Withdraw(2000)
    obj1.displayBalance()

if __name__ == "__main__":
    main()