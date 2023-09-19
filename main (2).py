# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the Deposit & Withdrawn Machine") 
 
    def deposit(self):
        Amount=float(input("Enter amount to be Deposited:"))
        self.balance += Amount
        print("\n Amount Deposited:",Amount)
 
    def withdraw(self):
        Amount = float(input("Enter Amount to be Withdrawn:"))
        if self.balance>=Amount:
            self.balance-=Amount
            print("\n You Withdrew:", Amount) 
        else:
            print("\n Insufficient balance")
 
    def display(self):
        print("\n Net Available Balance=",self.balance)
 
# Driver code
  
# creating an object of class
s= Bank_Account()
  
# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()