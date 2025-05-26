class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        return self.balance 

    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Not enough balance"
    

    def __str__(self):
        return f"BankAccount(owner: {self.owner}, balance: {self.balance})"
    


person1 = BankAccount("Philip")
person1.deposit(700)



print(person1)
print(person1.balance)

person1.withdraw(200)
print(person1.balance)


        