import random
from bank_account import BankAccount

print("Welcome to the Bank of Jack!")
print()

name = input("Please enter your name: ").strip()

while name == "" or not name.replace(" ", "").isalpha():
    print("Invalid name. Please use only letters.")
    name = input("Please enter your name: ").strip()

account_number = random.randint(10000, 99999)

account = BankAccount(name, account_number)

while True:
    print()
    print("Please choose an option:")
    print("1. Make a deposit")
    print("2. Make a withdrawal")
    print("3. View account information")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        while True:
            try:
                amount = float(input("How much would you like to deposit? "))
                if amount > 0:
                    account.deposit(amount)
                    break
                else:
                    print("Please enter an amount greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "2":
        while True:
            try:
                amount = float(input("How much would you like to withdraw? "))
                if amount > 0:
                    account.withdraw(amount)
                    break
                else:
                    print("Please enter an amount greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    elif choice == "3":
        account.display_info()

    elif choice == "4":
        print("Thank you for your business!")
        break

    else:
        print("Invalid choice. Please try again")



    