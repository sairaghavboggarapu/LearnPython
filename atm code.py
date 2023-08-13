
import pandas as pd
import datetime
import sys
class Customer:
    bankname='WELCOME TO INDIANBANK OF VUYYURU'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def amountcredit(self,amt):
        self.balance=self.balance+amt
        print('Balance after depositing:',self.balance)
        a=self.balance
    def withdraw(self,amt):
        if amt>self.balance:
            print('Insufficient Amount.....cannot perform this operation')
            sys.exit()
        else:
            self.balance=self.balance-amt
            print('Balance after withdrawing:',self.balance)
            b=self.balance
    def balance_enquiry(self,amt):
        print('Available balance is:',self.balance)
    def mini(self,amt):
        data = {"S.No":[1,2],
        "Type":["credit","debit"],
        "Date":[date,date],
        "Balance":[10000,6500]}
        myvar = pd.DataFrame(data)
        print(myvar)
        

print('Welcome to',Customer.bankname)
name=input('Enter Your Name:')
last_digits=input("Enter the last digits of ATM")
PIN=input("Enter the PIN")
c=Customer(name)
while True:
    print('1-Deposit \n2-Withdraw \n3-balance_enquiry\n4-mini statement\n5-exit')
    option=input('Choose your option:')
    date = datetime.datetime.now()
    if option=='1':
        amt=float(input('Enter amount:'))
        c.amountcredit(amt)
    elif option=='2':
        amt=float(input('Enter amount:'))
        c.withdraw(amt)
    elif option=='3':
        c.balance_enquiry(amt)
    elif option=='4':
        c.mini(amt)
        print("your minit statement is")
        
    elif option=='5':
        print('Thanks for Banking with INDIANBANK')
        sys.exit()
    else:
        print('Invalid option..Plz choose valid option')
