from pathlib import Path
from banking1 import Customer, SavingsAccount, CurrentAccount, user_details

# Create folder for transactions
new_folder = Path("my_folder")
new_folder.mkdir(exist_ok=True)

print("======= WELCOME TO MEDI-BANK =======")
print("""
How can we help you?
Select one of the following:
1. Create Account
2. Deposit
3. Withdraw
4. Check Balance
5. View Transactions
6. Exit
""")

user_option = input("Select an option (1–6): ").lower().strip()

if user_option in ("create account", "1"):
    name, age, occupation, account_type, balance = user_details()

    if account_type.lower() == "savings":
        acct = SavingsAccount(name, age, occupation, balance)
        print("\nAccount successfully created!")
    elif account_type.lower() == "current":
        acct = CurrentAccount(name, age, occupation, balance)
        print("\nAccount successfully created!")
    else:
        print("not available")


elif user_option in ("deposit", "2"):
    name, age, occupation, account_type, balance = user_details()
    if account_type.lower() == "savings":
        acct = SavingsAccount(name, age, occupation, balance)
    else:
        acct = CurrentAccount(name, age, occupation, balance)
    print(acct.deposit())

elif user_option in ("withdraw", "3"):
    name, age, occupation, account_type, balance = user_details()
    if account_type.lower() == "savings":
        acct = SavingsAccount(name, age, occupation, balance)
    else:
        acct = CurrentAccount(name, age, occupation, balance)
    print(acct.withdrawals())

elif user_option in ("check balance", "4"):
    name, age, occupation, account_type, balance = user_details()
    if account_type.lower() == "savings":
        acct = SavingsAccount(name, age, occupation, balance)
    else:
        acct = CurrentAccount(name, age, occupation, balance)
    print(acct.show_balance())

elif user_option in ("view transaction", "5"):
    name, age, occupation, account_type, balance = user_details()
    if account_type.lower() == "savings":
        acct = SavingsAccount(name, age, occupation, balance)
    else:
        acct = CurrentAccount(name, age, occupation, balance)
    print(acct.show_transaction())

    # Save transaction to text file
    file_path = Path(new_folder / f"{name}_transactions.txt")
    with open(file_path, "w") as file:
        file.write(acct.show_transaction())
    print(f"Transaction saved to: {file_path}")

elif user_option in ("exit", "6"):
    print("Thank you for choosing Medi-Bank. Goodbye!")
    exit()

else:
    print("Invalid selection! Please choose between 1 and 6.")
