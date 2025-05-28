
# Create a bank account
# Deposit money
# Withdraw money
# Show balance
# Exit


from BankCl import Bank

def menu2():
    print(f"\nWelcome to your current account {name}\n")
    print("-------------------------------------")
    print("1. View your balance")
    print("2. Deposit an amount")
    print("3. Withdraw an amount")
    print("4. Exit\n")


name = input("Enter your name: ")
balance = float(input("Enter your balance: "))
newAccount = Bank(name, balance)

print("-----------------------------------")
while True:
    menu2()
    choice = input("Enter your choice: ")
    if choice == "1":
        newAccount.show()

    elif choice == "2":
        amount = float(input("Enter your amount: "))
        newAccount.deposit(amount)

    elif choice == "3":
        amount = float(input("Enter your amount: "))
        newAccount.withdraw(amount)

    elif choice == "4":
        exit()
