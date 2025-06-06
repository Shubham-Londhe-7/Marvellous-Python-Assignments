
class BankAccount:
    ROI = 10.5

    def __init__(self, userName, userAmount):
        self.Name = userName
        self.Amount = userAmount

    def Display(self):
        print("User Name is : "+self.Name)
        print("Available Balance :",self.Amount)

    def Deposit(self,DepositAmount):
        self.Amount += DepositAmount
        print(DepositAmount,"Amount Deposited Successfully !!")
        print("Available balance :",self.Amount)

    def Withdraw(self,WithdrawAmount):
        if(self.Amount < WithdrawAmount):
            print("Insufficient Balance")
            return 
        self.Amount -= WithdrawAmount
        print(WithdrawAmount,"Amount Withdraw Successfully !!")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI)/100
        print("Interest for one year on amount :",self.Amount,"is :",Interest)


def main():
    print("Enter Name : ")
    name = input()
    print("Enter Amount :")
    amount = float(input())

    obj1 = BankAccount(name,amount)
    
    print("Enter amount to deposit :")
    amt = float(input())
    obj1.Deposit(amt)

    print("Enter amount to withdraw :")
    amt = float(input())
    obj1.Withdraw(amt)

    obj1.CalculateInterest()

if __name__ == "__main__":
    main()