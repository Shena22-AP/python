
class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)
        print("Updated balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print("Amount withdrawn:", amount)
            print("Updated balance:", self.balance)


# Getting account details
acc_no = input("Enter account number: ")
name = input("Enter name: ")
acc_type = input("Enter account type: ")
balance = float(input("Enter initial balance: "))

# Creating account object
account = BankAccount(acc_no, name, acc_type, balance)

# Deposit amount
deposit_amount = float(input("Enter amount to deposit: "))
account.deposit(deposit_amount)

# Withdraw amount
withdraw_amount = float(input("Enter amount to withdraw: "))
account.withdraw(withdraw_amount)
