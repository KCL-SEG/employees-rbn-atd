"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

from calendar import c


class Employee:
    def __init__(self, name, isContract, contractHours, pay, hasCommission, hasComContract, contractNo, commissionPay ):
        self.name = name
        self.isContract = isContract
        self.contractHours = contractHours
        self.pay = pay
        self.hasCommission = hasCommission
        self.hasComContract = hasComContract
        self.contractNo = contractNo
        self.commissionPay = commissionPay
        

    def get_pay(self):
        totalPay = 0
        if (self.isContract):
            totalPay = (self.contractHours * self.pay) + self.calculate_commission()
        else:
            totalPay = self.pay + self.calculate_commission()
        return totalPay

    def calculate_commission(self):
        totalCom = 0
        if (self.hasComContract):
            totalCom = self.contractNo*self.commissionPay     
        else:
            totalCom = self.commissionPay
        return totalCom

    def __str__(self):
        if (self.isContract):
           self.str_contract()
        else:
            self.str_monthly()
        return ""

    def str_contract(self):
        if(self.hasCommission and self.hasComContract ):
            print( f"{self.name} works on a contract of {self.contractHours} hours at {self.pay}/hour and recieves a commission for {self.contractNo} contract(s) at {self.commissionPay}/contract.  Their total pay is { self.get_pay() }." )
        elif(self.hasCommission and not self.hasComContract):
            print( f"{self.name} works on a contract of {self.contractHours} hours at {self.pay}/hour and receives a bonus commission of {self.commissionPay}. Their total pay is {self.get_pay()}." )
        else:
            print( f"{self.name} works on a contract of {self.contractHours} hours at {self.pay}/hour. Their total pay is {self.get_pay()}")

    def str_monthly(self):
        if(self.hasCommission and self.hasComContract):
            print( f"{self.name} works on a monthly salary of {self.pay} and receives a commission for {self.contractNo} contract(s) at {self.commissionPay}/contract.  Their total pay is { self.get_pay() }." )
        elif(self.hasCommission and not self.hasComContract):
            print( f"{self.name} works on a monthly salary of {self.pay} and recieves a bonus commission of {self.commissionPay}. Their total pay is { self.get_pay() }." )
        else:
            print( f"{self.name} works on a monthly salary of {self.pay}. Their total pay is {self.get_pay()}.")

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, None, 4000, False, False, None, 0)

# Charlie works on a contract of 100 contractHours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', True, 100, 25, False, False, None, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', False, None, 3000, True, True, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 150, 25, True, True, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', False, None, 2000, True, False, None, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 120, 30, True, False, None, 600)

print(billie.get_pay())
str(billie)