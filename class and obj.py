class BankAccount:
    next_account_number = 1001

    def __init__(self, name, starting_balance):
        self.name = name
        self.account_number = BankAccount.next_account_number
        self.balance = starting_balance
        BankAccount.next_account_number += 1

    def show_balance(self):
        print(f"{self.name}'s balance: {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")

        self.balance -= amount
        print(f"Withdrew {amount}. New balance: {self.balance}")


account1 = BankAccount("Sajit", 100)
account2 = BankAccount("Alex", 250)

print(f"{account1.name}'s account number: {account1.account_number}")
account1.show_balance()
account1.deposit(50)
account1.withdraw(30)

print(f"{account2.name}'s account number: {account2.account_number}")
account2.show_balance()
