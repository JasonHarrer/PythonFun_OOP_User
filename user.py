#!/usr/bin/env python

class User:
    def __init__(self, username, email_address):
        self.name            = username
        self.email           = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f'User: {self.name}: ${self.account_balance}')
        if self.account_balance < 0:
            print('*** THIS ACCOUNT IS OVERDRAFTED ***')

    def transfer_money(self, other_user, amount):
       self.make_withdrawal(amount)
       other_user.make_deposit(amount)


# Test section
jeremy = User("Jeremy Fakename", "jeremy@fakename.com")
alice  = User("Alice I'dunno",   "alice@somecompany.com")
mickey = User("Mickey Mickey",   "youre@sofine.org")

#Test 1: Have the first user make 3 deposits and 1 withdrawal and then display their balance
jeremy.make_deposit(200)
jeremy.make_deposit(300)
jeremy.make_deposit(500)
jeremy.make_withdrawal(800)
jeremy.display_user_balance()


#Test 2: Have the second user make 2 deposits and 2 withdrawals and then display their balance
alice.make_deposit(500)
alice.make_deposit(400)
alice.make_withdrawal(650)
alice.make_withdrawal(100)
alice.display_user_balance()


#Test 3: Have the third user make 1 deposit and 3 withdrawals and then display their alance
mickey.make_deposit(500)
mickey.make_withdrawal(200)
mickey.make_withdrawal(100)
mickey.make_withdrawal(300)
mickey.display_user_balance()


#Test 4: Have the first user transfer money to the third user and then print both users' balances'
jeremy.transfer_money(mickey, 100)
jeremy.display_user_balance()
mickey.display_user_balance()
