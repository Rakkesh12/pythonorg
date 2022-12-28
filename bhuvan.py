"""try:
    a=int(input())
    #print(s)
    b=int(input())
    c=a%b
    print(c)
except:
    #print("error occured")
    print("if {0}/{1} error occured".format(a,b))
finally:
    print("program completed")"""

class high_exception(Exception):
    pass

class Bank:
    def __init__(self,balance,deposit,withdraw):
        self.balance=balance
        self.deposit=deposit
        self.withdraw=withdraw
    def balance_amount(self):
        try:
            if (self.balance>0):
                print(self.balance)
            else:
                raise OverflowError
        except OverflowError:
            print("balance is insufficent")
        finally:
            print("balance is checked")
    def deposit_amount(self):
        try:
            if(self.deposit<2000):
                self.balance+=self.deposit
                print("after depositing the amount {}".format(self.balance))
            else:
                raise OverflowError
        except OverflowError:
            print("daily deposit is less than 2000")
        finally:
           print("deposited amount {}".format(self.deposit))
    def withdraw_amount(self):
        try:
            if(self.withdraw<500):
                self.balance=self.balance-self.withdraw
                print(self.balance)
            else:
                raise high_exception
        except high_exception:
            print("withdraw amount should be less tha 500 daily")



obj_1=Bank(20,5000,200)
obj_1.balance_amount()
obj_1.deposit_amount()
obj_1.withdraw_amount()