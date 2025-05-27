class Bank:
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance


    def deposit(self, amount):
        self.balance+=amount
        print(f"{amount} deposited successfully")
        print(f"New balance: {self.balance}")


    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully")
            print(f"new balance is: £{self.balance}")

    def show(self):
        print(f"Current balance is: {self.balance}")



