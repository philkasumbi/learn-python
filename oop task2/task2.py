owner = input("Enter your name:")
account_number = int(input("Enter your Account number:"))

class BankAccount:
    def __init__(self,owner,account_number,balance=0):
        self.owner= owner
        self.account_number = account_number
        self.balance = balance
        
    def create_account(self):
     owner = input("Enter your name:")
     account_number = int(input("Enter your Account number:"))
     print(f"The owner is {owner} and the owners account number is {account_number}")  
    

    def deposit(self,amount):
        amount = int(input("Enter the amount you wish to deposit: "))
        self.balance +=amount
        print(f"Successifully deposited: ${amount}")
        return self.balance
        
        
    
    def withdraw(self,amount):
        amount = int(input("Enter the amount you wish to withdraw: "))
        if 0 < amount <= self.balance:
            self.balance -=amount
            print(f"Successifully withdrew: ${amount}")
            return self.balance
        else:
            print(f"You cannot withdraw ${amount}")
            
    def check_balance(self):
        print(f"{self.owner} your account {self.account_number} has a balance of ${self.balance}")


    def transfer(self,transferamount,target_account):
        self.transferamount = transferamount
        self.target_account = target_account
        
        transferamount = int(input("Enter the amount you wish to Transfer: "))
        target_account = int(input("Enter the account you wish to Transfer To: "))
        if 0 < transferamount <= self.balance:
            target_account += transferamount
            self.balance -= transferamount
            print(f"You have successifully transfered ${transferamount} to {target_account}")
            

        else:
            print(f"You cannot transfer ${transferamount} to {target_account} ")

   


person = BankAccount(owner,account_number)

accounts = {}

accounts[owner] = person


def show_menu():
        print("""
===== LIST MENU =====
1. Check Balance
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Exit
6. Create Account
""")
while True:
    show_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
         person.check_balance()
    elif choice == "2":
         person.deposit(500)
    elif choice == "3":
         person.withdraw(300)
    elif choice == "4":
         person.transfer(transferamount=[],target_account=[])
    elif choice == "5":
         print("Good bye")
         break
    elif choice == "6":
         person.create_account()
    else:
          print("Invalid choice, Please try again")




