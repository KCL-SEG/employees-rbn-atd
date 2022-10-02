"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.stringCheck()

class ContractEmployee(Employee):
    def __init__(self, name, contractHours, hourlyWage):
        super().__init__(name)
        self.contractHours = contractHours
        self.hourlyWage = hourlyWage

    def get_pay(self):
        return self.contractHours*self.hourlyWage

    def stringCheck(self):
        return (f"{self.name} works on a contract of {self.contractHours} hours at {self.hourlyWage}/hour.  Their total pay is {self.get_pay()}.")

class ContractBonusEmployee(ContractEmployee):
    def __init__(self, name, contractHours, hourlyWage, bonus):
        super().__init__(name, contractHours, hourlyWage)
        self.bonus = bonus
    
    def get_pay(self):
        return super().get_pay() + self.bonus

    def stringCheck(self):
       return (f"{self.name} works on a contract of {self.contractHours} hours at {self.hourlyWage}/hour and receives a bonus commission of {self.bonus}.  Their total pay is {self.get_pay()}." )

class ContractCommissionEmployee(ContractEmployee):
    def __init__(self, name, contractHours, hourlyWage, commissionContracts, commissionWage):
        super().__init__(name, contractHours, hourlyWage)
        self.commissionContracts = commissionContracts
        self.commissionWage = commissionWage

    def get_pay(self):
        return super().get_pay() + (self.commissionContracts*self.commissionWage)

    def stringCheck(self):
        return (f"{self.name} works on a contract of {self.contractHours} hours at {self.hourlyWage}/hour and receives a commission for {self.commissionContracts} contract(s) at {self.commissionWage}/contract.  Their total pay is { self.get_pay() }." )

class SalaryEmployee(Employee):
    def __init__(self, name, monthlySalary):
        super().__init__(name)
        self.monthlySalary = monthlySalary

    def get_pay(self):
        return self.monthlySalary

    def stringCheck(self):
        return ( f"{self.name} works on a monthly salary of {self.monthlySalary}.  Their total pay is {self.get_pay()}.")

class SalaryBonusEmployee(SalaryEmployee):
    def __init__(self, name, monthlySalary, bonus):
        super().__init__(name, monthlySalary)
        self.bonus = bonus

    def get_pay(self):
        return super().get_pay() + self.bonus

    def stringCheck(self):
        return (f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a bonus commission of {self.bonus}.  Their total pay is { self.get_pay() }." )

class SalaryCommissionEmployee(SalaryEmployee):
    def __init__(self, name, monthlySalary, commissionContracts, commissionWage):
        super().__init__(name, monthlySalary)
        self.commissionContracts = commissionContracts
        self.commissionWage = commissionWage
    
    def get_pay(self):
        return super().get_pay() + (self.commissionContracts*self.commissionWage)
    
    def stringCheck(self):
        return (f"{self.name} works on a monthly salary of {self.monthlySalary} and receives a commission for {self.commissionContracts} contract(s) at {self.commissionWage}/contract.  Their total pay is { self.get_pay() }." )
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 contractHours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryCommissionEmployee('Renee', 3000, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractCommissionEmployee('Jan', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryBonusEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractBonusEmployee('Ariel', 30, 120, 600)


print(str(renee))