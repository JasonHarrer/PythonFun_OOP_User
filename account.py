#!/usr/bin/env python

class BankAccount:
    def __init__(self, starting_balance=0.00,
                       starting_interest_rate=0.025):
        self.balance       = starting_balance
        self.interest_rate = starting_interest_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f'Balance: {self.balance}')
        return self

    def yield_interest(self):
        self.balance += (self.balance * self.interest_rate)
        return self


# Test 1:  Create 2 accounts
account1 = BankAccount()
account2 = BankAccount(100, 0.032)

# Test 2: To the first account, make 3 deposits & 1 withdrawal, then
#         calculate interest and display the account's info all in one
#         line of code.
account1.deposit(500).deposit(600).deposit(550).withdraw(450).yield_interest().display_account_info()

# Test 3: To the second account, make 2 deposits and 4 withdrawals, then
#         calculate and display the account's info all in one line of
#         code.
account2.deposit(500).deposit(400).withdraw(300).withdraw(300).withdraw(300).withdraw(300).display_account_info()
