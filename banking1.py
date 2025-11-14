# to input customers details
from datetime import datetime

    
def user_details():
    name= input("user name: ")
    while True:
        try:
            age= int(input("users age: "))
            if age > 0:
                break
            else:
                print("age cannot be zero!")
        except ValueError:
            print("age must be a whole number")
    occupation=input("your occupation: ")
    account_type=input("type of account to be created (SAVINGS OR CURRENT): ")
    balance=0
    return name, age, occupation, account_type,balance


class Customer:
    def __init__(self, name, age, occupation, account_type, balance):
        self.name = name
        self.age = age
        self.occupation = occupation
        self.account_type = account_type
        self.balance = balance
        self.transactions = []

    def deposit(self):
        amount = int(input("Deposit amount: "))
        if amount > 0:
            self.balance += amount
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(f"[{timestamp}] Deposited ₦{amount} | New Balance: ₦{self.balance}")
            return f"Deposit successful. New balance: ₦{self.balance}"
        else:
            return "Deposit must be greater than zero."

    def withdrawals(self):
        amount = int(input("Withdrawal amount: "))
        if amount > self.balance:
            return "Insufficient balance."
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            self.balance -= amount
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(f"[{timestamp}] Withdrew ₦{amount} | New Balance: ₦{self.balance}")
            return f"Withdrawal successful. New balance: ₦{self.balance}"

    def show_transaction(self):
        if not self.transactions:
            return f"No transactions yet for {self.name}."
        else:
            records = "\n".join(self.transactions)
            return f"""=========MEDI-BANK==========
==== TRANSACTION HISTORY ====
Account Holder: {self.name}
{records}
============================"""


class SavingsAccount(Customer):
    def __init__(self, name, age, occupation, balance, interest_rate=0.05):
        super().__init__(name, age, occupation, "Savings", balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        self.transactions.append(f"[{timestamp}] Interest Added ₦{interest:.2f} | New Balance: ₦{self.balance:.2f}")
        return f"Interest of ₦{interest:.2f} added successfully."


class CurrentAccount(Customer):
    def __init__(self, name, age, occupation, balance, overdraft_limit=5000):
        super().__init__(name, age, occupation, "Current", balance)
        self.overdraft_limit = overdraft_limit

    def withdrawals(self):
        amount = int(input("Withdrawal amount: "))
        if amount <= 0:
            return "Invalid withdrawal amount."
        elif amount > self.balance + self.overdraft_limit:
            return "Overdraft limit exceeded."
        else:
            self.balance -= amount
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            self.transactions.append(f"[{timestamp}] Withdrew ₦{amount} | New Balance: ₦{self.balance}")
            return f"Withdrawal successful. New balance: ₦{self.balance}"