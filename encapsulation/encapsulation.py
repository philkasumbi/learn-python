class BankAccount:
    def __init__(self,balance):
        self.__balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}")
        else:
            print("Deposit must be positive")

    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"withdrew {amount}")
        else:
            print("Invalid amount or insufficient funds")

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)

account.deposit(250)
account.withdraw(500)
print(f"current balance ${account.get_balance()}")

# print(__balance)-trying to access balance outside the class will cause an attribute error

"""
create a vehicle class and a car class that inherits from it 
make sure that the car class has a private attribute eg fuel level 
and methods to add fuel to the car and check fuel level 
"""