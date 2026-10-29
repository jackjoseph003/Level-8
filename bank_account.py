
class BankAccount:
    def __init__(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.00

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print()
            print("Deposit successful")
            print()
        else:
            print()
            print("Invalid deposit amount.")
            print()

    def withdraw(self, amount):
        if amount <= 0:
            print()
            print("Invalid withdrawal amount.")
            print()
        elif amount > self.balance:
            print()
            print("Insufficient funds.")
            print()
        else:
            self.balance -= amount
            print()
            print("Withdrawal successful!")
            print()

    def display_info(self):
        print()
        print(f"Name: {self.name}")
        print(f"Account: #{self.account_number}")
        print(f"Balance: ${self.balance:.2f}")
        print()
