#!/usr/bin/env python

class User:
    def __init__(self, username, email_address):
        self.name            = username
        self.email           = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f'User: {self.name}: ${self.account_balance}')
        if self.account_balance < 0:
            print('*** THIS ACCOUNT IS OVERDRAFTED ***')
        return self

    def transfer_money(self, other_user, amount):
       self.make_withdrawal(amount)
       other_user.make_deposit(amount)
       return self


# Test section
jeremy = User("Jeremy Fakename", "jeremy@fakename.com")
alice  = User("Alice I'dunno",   "alice@somecompany.com")
mickey = User("Mickey Mickey",   "youre@sofine.org")

#Test 1: Have the first user make 3 deposits and 1 withdrawal and then display their balance
jeremy.make_deposit(200).make_deposit(300).make_deposit(500).make_withdrawal(800).display_user_balance()


#Test 2: Have the second user make 2 deposits and 2 withdrawals and then display their balance
alice.make_deposit(500).make_deposit(400).make_withdrawal(650).make_withdrawal(100).display_user_balance()


#Test 3: Have the third user make 1 deposit and 3 withdrawals and then display their alance
mickey.make_deposit(500).make_withdrawal(200).make_withdrawal(100).make_withdrawal(300).display_user_balance()


#Test 4: Have the first user transfer money to the third user and then print both users' balances'
jeremy.transfer_money(mickey, 100).display_user_balance()
mickey.display_user_balance()
