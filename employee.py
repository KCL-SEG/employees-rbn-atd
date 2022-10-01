"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, isHourly, contractHours, pay, commission ):
        self.name = name
        self.isHourly = isHourly
        self.contractHours = contractHours
        self.pay = pay
        self.commission = commission

    def get_pay(self):
        totalPay = 0
        if (self.isHourly == True):
            totalPay = (self.contractHours * self.pay) + self.commission
        else:
            totalPay = self.pay + self.commission
        return totalPay
            

    def __str__(self):
        return self.name


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', False, None, 4000, 0)

# Charlie works on a contract of 100 contractHours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', True, 100, 25, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', False, None, 3000, 800)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', True, 150, 25, 660)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', False, None, 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', True, 120, 30, 600)


print(robbie.get_pay())